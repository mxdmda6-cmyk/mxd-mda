"""
🜂 Store Manager Module

Claude-powered Lead E-Commerce Manager and Brand Custodian for the
MXD MDA (Mixed Media) Shopify storefront.

Two modes:

1. Copy-only (no tools) — import and call :func:`chat_with_store_manager`
   for on-brand drafting (listings, SOPs, customer replies). No Shopify
   connection required.

       from orchestrator.store_manager import chat_with_store_manager
       print(chat_with_store_manager("Draft a listing for the Crow Codex print."))

2. Live operations — run this module as a script to open an interactive
   session wired to a Shopify MCP server. Claude connects to the store
   through a local MCP client and calls tools (products, orders, inventory,
   analytics) to ground its answers, with a write guardrail.

       export ANTHROPIC_API_KEY=...
       export SHOPIFY_MCP_URL=https://<your-shopify-mcp>/sse
       export SHOPIFY_ALLOW_WRITES=false      # default; true to permit writes
       python src/orchestrator/store_manager.py

Environment:
    ANTHROPIC_API_KEY    Required (resolved by the SDK).
    SHOPIFY_MCP_URL      Required for live mode — the MCP server SSE endpoint.
    SHOPIFY_MCP_TOKEN    Optional — sent as an OAuth bearer token.
    SHOPIFY_ALLOW_WRITES Optional — "true"/"1"/"yes" to permit write tools.

Live mode requires the ``mcp`` package (``pip install mcp``); copy-only mode
does not.
"""

from __future__ import annotations

import asyncio
import json
import os
from typing import Any

import anthropic
from anthropic import AsyncAnthropic

# Default to the most capable Opus-tier model. The retired
# claude-3-5-sonnet-20241022 (sunset 2025-10-28) is intentionally not used.
MODEL = "claude-opus-4-8"
MAX_TOKENS = 4096

# Bound the agentic loop so a misbehaving turn can't call tools forever.
MAX_TOOL_STEPS = 8

# Known Shopify MCP tools that create, mutate, or delete store state. Used as
# an explicit denylist; the prefix heuristic below catches dynamic/unknown
# write tools too. Names match the Shopify MCP server's tool identifiers.
SHOPIFY_WRITE_TOOLS = frozenset(
    {
        "create-product",
        "update-product",
        "bulk-update-product-status",
        "create-collection",
        "update-collection",
        "add-to-collection",
        "create-discount",
        "set-inventory",
        "switch-shop",
        "graphql_mutation",
        "get-new-store-previews",
    }
)

# Verb prefixes that imply a mutating operation. Matched against the tool name
# after normalizing hyphens to underscores, so "create-product" and
# "create_product" are both caught.
_WRITE_PREFIXES = (
    "create",
    "update",
    "delete",
    "set",
    "adjust",
    "cancel",
    "mark",
    "add",
    "remove",
    "bulk",
    "publish",
    "archive",
    "switch",
)

_NORMALIZED_WRITE_TOOLS = frozenset(
    name.replace("-", "_") for name in SHOPIFY_WRITE_TOOLS
)


# The system prompt establishes Claude's role, brand voice, and operational
# rules. Kept frozen (no per-request interpolation) so it caches cleanly.
STORE_MANAGER_SYSTEM_PROMPT = """
Act as the Lead E-Commerce Manager and Brand Custodian for MXD MDA (Mixed \
Media). Your primary directive is to manage, optimize, and help run our \
Shopify storefront. You will assist with daily operations, product listings, \
inventory management, customer communications, and marketing strategies.

Brand Context & Voice:
- Brand Identity: MXD MDA is a hybrid creative studio specializing in \
transmedia storytelling, blending esoteric knowledge, gothic-noir \
aesthetics, and modern innovation.
- Tone & Voice: You must embody the "Mystical Bridge-Builder." Your tone in \
customer-facing copy should be contemplative, illuminating, gently \
authoritative, and mystical yet grounded. In our internal operational \
discussions, be highly analytical, precise, and strategic.
- Visual Aesthetics: Oil paint realism, vintage etching, gothic, alchemical \
symbolism, utilizing our primary colors (Gold, Deep Black) and secondary \
colors (Warm Beige, Metallic Silver).

Core Responsibilities & Workflows:
1. Product Management: Write compelling, SEO-optimized product descriptions \
for physical merchandise and digital art prints. Ensure copy reflects the \
deeper, interconnected narratives of the brand.
2. Operations & Fulfillment: Troubleshoot Printify-to-Shopify syncing issues \
and draft standard operating procedures (SOPs).
3. Customer Experience: Draft email templates and formulate thoughtful, \
on-brand responses to customer service inquiries.
4. Strategic Growth: Analyze sales data and plan promotional cadences.

Operational Directives:
- Return a drafted title, a 3-4 sentence immersive description, bullet points \
for technical specs, and 5-10 SEO keywords for product descriptions.
- Provide step-by-step, actionable solutions for technical issues.
- Explicitly ask for missing crucial information before generating a final \
response.

Live Store Operations (when Shopify tools are available):
- Verify facts with your Shopify tools before reporting them; never guess \
inventory counts, prices, or order status.
- Keep operational reporting concise, precise, and professional.
- Before any action that changes store data (price, inventory, product, \
collection, discount, or order state), state plainly what you are about to \
change and why, then proceed.
""".strip()


def _env_flag(name: str) -> bool:
    """Return True when an env var is set to a truthy string."""
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def is_write_operation(tool_name: str) -> bool:
    """Heuristically decide whether a tool name mutates store state.

    Combines an explicit denylist with a verb-prefix check on the
    separator-normalized name, plus a catch-all for GraphQL mutations.
    """
    norm = tool_name.strip().lower().replace("-", "_")
    if norm in _NORMALIZED_WRITE_TOOLS or "mutation" in norm:
        return True
    return norm.split("_", 1)[0] in _WRITE_PREFIXES


def _client(api_key: str | None = None) -> anthropic.Anthropic:
    """Build a sync Anthropic client.

    Resolves credentials from ``ANTHROPIC_API_KEY`` (or an ``ant`` profile)
    by default; pass ``api_key`` only when you must inject a specific key.
    """
    if api_key:
        return anthropic.Anthropic(api_key=api_key)
    return anthropic.Anthropic()


def _text(response: anthropic.types.Message) -> str:
    """Concatenate the text blocks of a response (skips thinking/tool blocks)."""
    return "\n".join(
        block.text for block in response.content if block.type == "text"
    ).strip()


def chat_with_store_manager(
    user_message: str,
    *,
    client: anthropic.Anthropic | None = None,
    max_tokens: int = MAX_TOKENS,
) -> str:
    """Draft an on-brand reply from the Store Manager persona (no tools).

    Args:
        user_message: The operator or customer-facing request.
        client: Optional pre-built Anthropic client (handy for tests/reuse).
        max_tokens: Output token ceiling for the reply.

    Returns:
        The assistant's text response, or an error string on failure.

    Note:
        Creativity-vs-precision is steered through the system prompt and
        adaptive thinking rather than ``temperature`` — sampling parameters
        are not supported on Opus 4.8 and would raise a 400. For live store
        access, run this module as a script (see :func:`run_orchestrator`).
    """
    client = client or _client()
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=STORE_MANAGER_SYSTEM_PROMPT,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": user_message}],
        )
    except anthropic.APIError as exc:
        return f"An error occurred: {exc}"
    return _text(response)


# --------------------------------------------------------------------------- #
# Live operations: local MCP client + manual agentic loop
# --------------------------------------------------------------------------- #


def _preview(value: Any, limit: int = 80) -> str:
    """Render a compact, truncated preview of tool input for logging."""
    try:
        text = json.dumps(value, separators=(",", ":"), default=str)
    except (TypeError, ValueError):
        text = str(value)
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _mcp_result_text(result: Any) -> str:
    """Flatten an MCP CallToolResult into text for a tool_result block."""
    items = getattr(result, "content", None) or []
    parts = [getattr(item, "text", None) or str(item) for item in items]
    return "\n".join(parts).strip() or "(tool returned no content)"


async def _execute_tool(
    mcp_session: Any, block: Any, *, allow_writes: bool
) -> dict[str, Any]:
    """Run one tool call via MCP, enforcing the write guardrail."""
    if is_write_operation(block.name) and not allow_writes:
        print(f"  ⚠️  Blocked write '{block.name}' (SHOPIFY_ALLOW_WRITES=false)")
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": (
                "Error: Write operations are disabled. Tell the user they must "
                "set SHOPIFY_ALLOW_WRITES=true to perform this action."
            ),
            "is_error": True,
        }

    print(f"  ⚡ {block.name}({_preview(block.input)})")
    try:
        result = await mcp_session.call_tool(block.name, block.input)
    except Exception as exc:  # noqa: BLE001 - surface any tool failure to Claude
        return {
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": f"Tool execution failed: {exc}",
            "is_error": True,
        }
    return {
        "type": "tool_result",
        "tool_use_id": block.id,
        "content": _mcp_result_text(result),
        "is_error": bool(getattr(result, "isError", False)),
    }


async def _run_agent_turn(
    client: AsyncAnthropic,
    mcp_session: Any,
    tools: list[dict[str, Any]],
    messages: list[dict[str, Any]],
    *,
    allow_writes: bool,
) -> str:
    """Drive one user turn to completion, executing tool calls along the way.

    Loops until Claude stops requesting tools (``end_turn``), handling multiple
    tool_use blocks per response and bounded by :data:`MAX_TOOL_STEPS`.
    """
    for _ in range(MAX_TOOL_STEPS):
        response = await client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=STORE_MANAGER_SYSTEM_PROMPT,
            thinking={"type": "adaptive"},
            tools=tools,
            messages=messages,
        )
        # Append full content (incl. thinking) so the turn replays cleanly.
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            return _text(response)

        results = [
            await _execute_tool(mcp_session, block, allow_writes=allow_writes)
            for block in response.content
            if block.type == "tool_use"
        ]
        messages.append({"role": "user", "content": results})

    return "Reached the maximum number of tool steps for this turn."


async def _chat_loop(
    client: AsyncAnthropic,
    mcp_session: Any,
    tools: list[dict[str, Any]],
    *,
    allow_writes: bool,
) -> None:
    """Interactive read-eval-print loop over a live MCP session."""
    messages: list[dict[str, Any]] = []
    print("\n🤖 MXD-MDA Operations ready. Type 'exit' to quit.")
    print("-" * 50)

    while True:
        user_input = (await asyncio.to_thread(input, "\nManager Input: ")).strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Shutting down operations manager. Goodbye!")
            return
        if not user_input:
            continue

        checkpoint = len(messages)
        messages.append({"role": "user", "content": user_input})
        try:
            reply = await _run_agent_turn(
                client, mcp_session, tools, messages, allow_writes=allow_writes
            )
            print(f"\nAI: {reply}")
        except anthropic.APIError as exc:
            print(f"\n❌ Operation failed: {exc}")
            # Roll back the whole failed turn so history stays consistent
            # (no dangling tool_use without a matching tool_result).
            del messages[checkpoint:]


async def _serve_session(
    client: AsyncAnthropic,
    streams: Any,
    *,
    allow_writes: bool,
    flag: dict[str, bool],
) -> None:
    """Run an interactive session over an established MCP transport.

    ``flag["connected"]`` is set once the session initializes, so the caller
    can distinguish a connection failure (try the next transport) from an
    error after a successful connect (report it, don't retry).

    ``streams`` may be a 2-tuple (SSE) or 3-tuple (Streamable HTTP); only the
    first two — the read and write streams — are used.
    """
    from mcp.client.session import ClientSession

    async with ClientSession(streams[0], streams[1]) as mcp_session:
        await mcp_session.initialize()
        flag["connected"] = True
        print("✅ Connected to Shopify MCP server.")

        listed = await mcp_session.list_tools()
        tools = [
            {
                "name": tool.name,
                "description": tool.description or "",
                "input_schema": tool.inputSchema,
            }
            for tool in listed.tools
        ]
        writeable = sum(1 for t in tools if is_write_operation(t["name"]))
        print(f"🛠️  {len(tools)} tools loaded ({writeable} write-capable).")
        print(f"🔒 Write operations allowed: {allow_writes}")

        await _chat_loop(client, mcp_session, tools, allow_writes=allow_writes)


async def _try_transport(
    client: AsyncAnthropic,
    open_transport: Any,
    url: str,
    headers: dict[str, str] | None,
    *,
    allow_writes: bool,
    label: str,
) -> bool:
    """Attempt one transport. Return True if it connected (so don't try others).

    A failure *before* connecting returns False so the caller can fall back; a
    failure *after* connecting is reported here and still returns True.
    """
    flag = {"connected": False}
    print(f"📡 Attempting {label} connection...")
    try:
        async with open_transport(url, headers=headers) as streams:
            await _serve_session(client, streams, allow_writes=allow_writes, flag=flag)
        return True
    except Exception as exc:  # noqa: BLE001 - decide retry vs. report
        if flag["connected"]:
            print(f"❌ Session error after connecting via {label}: {exc}")
            return True
        print(f"⚠️  {label} connection failed: {exc}")
        return False


async def run_orchestrator() -> None:
    """Connect Claude to the Shopify MCP server and start an interactive session.

    Tries SSE first, then falls back to Streamable HTTP. Fallback applies only
    to connection failures — an error after a successful connect is reported,
    not retried on the other transport.
    """
    url = os.environ.get("SHOPIFY_MCP_URL", "").strip()
    if not url:
        print("SHOPIFY_MCP_URL is not set; set it to enable live store access.")
        return
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY is not set; set it before running.")
        return

    try:
        from mcp.client.sse import sse_client
    except ImportError:
        print("The 'mcp' package is required for live mode: pip install mcp")
        return
    try:
        from mcp.client.streamable_http import streamablehttp_client
    except ImportError:
        streamablehttp_client = None

    allow_writes = _env_flag("SHOPIFY_ALLOW_WRITES")
    headers: dict[str, str] = {}
    token = os.environ.get("SHOPIFY_MCP_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    hdrs = headers or None

    print("🔌 Initializing MXD-MDA Operations Manager...")
    client = AsyncAnthropic()

    transports: list[tuple[str, Any]] = [("SSE", sse_client)]
    if streamablehttp_client is not None:
        transports.append(("Streamable HTTP", streamablehttp_client))

    for index, (label, open_transport) in enumerate(transports):
        if await _try_transport(
            client, open_transport, url, hdrs, allow_writes=allow_writes, label=label
        ):
            return
        if index + 1 < len(transports):
            print("🔄 Falling back to the next transport...")

    print("❌ Could not connect to the Shopify MCP server on any transport.")
    print(
        "Verify SHOPIFY_MCP_URL is reachable from this host and "
        "SHOPIFY_MCP_TOKEN (if required) is valid."
    )


def _main() -> None:
    """Run live operations if a Shopify MCP server is configured, else a demo."""
    if os.environ.get("SHOPIFY_MCP_URL", "").strip():
        asyncio.run(run_orchestrator())
        return

    print("Initializing MXD MDA Store Manager (copy-only mode)...")
    print("Set SHOPIFY_MCP_URL to enable live store operations.\n")
    print("-" * 50)
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY is not set; set it before running this demo.")
        return

    initial_prompt = (
        "Acknowledge these instructions by briefly summarizing your role and "
        "outlining the first three steps we should take to ensure the 'First "
        "Drop' collection is fully optimized for launch."
    )
    print(f"User Request: {initial_prompt}\n")
    print("-" * 50)
    print("Claude (Store Manager) is composing...\n")
    print(chat_with_store_manager(initial_prompt))


if __name__ == "__main__":
    _main()
