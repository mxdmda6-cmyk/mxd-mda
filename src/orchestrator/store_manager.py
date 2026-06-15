"""
🜂 Store Manager Module

Claude-powered Lead E-Commerce Manager and Brand Custodian for the
MXD MDA (Mixed Media) Shopify storefront.

Handles daily commerce operations through a single, brand-consistent persona:
- Product listings (SEO-optimized, on-brand copy)
- Operations & fulfillment SOPs (Printify ↔ Shopify)
- Customer-experience templates and responses
- Strategic growth (sales analysis, promotional cadence)

Usage:
    from orchestrator.store_manager import chat_with_store_manager

    reply = chat_with_store_manager("Write a listing for the Crow Codex print.")
    print(reply)

Live Shopify access (optional):
    Set ``SHOPIFY_MCP_URL`` to a remote Shopify MCP server (HTTPS) and the
    persona gains read access to the store via the Anthropic MCP connector —
    it can look up products, orders, customers, inventory, and analytics
    instead of only drafting copy. Set ``SHOPIFY_MCP_TOKEN`` if the server
    requires an OAuth bearer token.

    Writes are OFF by default (destructive/mutating tools are denylisted), in
    line with the project's posture that live store changes stay disabled
    unless intentionally activated. Set ``SHOPIFY_ALLOW_WRITES=true`` to let
    the persona create/update products, collections, discounts, and inventory.

Environment:
    ANTHROPIC_API_KEY   Required (resolved by the SDK).
    SHOPIFY_MCP_URL     Optional — enables live Shopify tools when set.
    SHOPIFY_MCP_TOKEN   Optional — OAuth bearer token for the MCP server.
    SHOPIFY_ALLOW_WRITES Optional — "true"/"1"/"yes" to permit write tools.
"""

from __future__ import annotations

import os
from typing import Any

import anthropic

# Default to the most capable Opus-tier model. The retired
# claude-3-5-sonnet-20241022 (sunset 2025-10-28) is intentionally not used.
MODEL = "claude-opus-4-8"
MAX_TOKENS = 4096

# Beta header for the remote MCP connector (mcp_servers + mcp_toolset).
MCP_BETA = "mcp-client-2025-11-20"

# Shopify MCP tools that create, mutate, or delete store state. Denylisted
# unless SHOPIFY_ALLOW_WRITES is enabled, keeping the persona read-only by
# default. Names match the Shopify MCP server's tool identifiers.
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


def _env_flag(name: str) -> bool:
    """Return True when an env var is set to a truthy string."""
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def _shopify_mcp_config() -> tuple[list[dict[str, Any]], list[dict[str, Any]]] | None:
    """Build (mcp_servers, tools) for the Shopify MCP connector.

    Returns None when ``SHOPIFY_MCP_URL`` is unset, in which case the persona
    runs without live store access. When writes are disabled (the default),
    every tool in :data:`SHOPIFY_WRITE_TOOLS` is denylisted.
    """
    url = os.environ.get("SHOPIFY_MCP_URL", "").strip()
    if not url:
        return None

    server: dict[str, Any] = {"type": "url", "url": url, "name": "shopify"}
    token = os.environ.get("SHOPIFY_MCP_TOKEN", "").strip()
    if token:
        server["authorization_token"] = token

    toolset: dict[str, Any] = {"type": "mcp_toolset", "mcp_server_name": "shopify"}
    if not _env_flag("SHOPIFY_ALLOW_WRITES"):
        toolset["configs"] = {
            name: {"enabled": False} for name in sorted(SHOPIFY_WRITE_TOOLS)
        }
    return [server], [toolset]


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
""".strip()


def _client(api_key: str | None = None) -> anthropic.Anthropic:
    """Build an Anthropic client.

    Resolves credentials from ``ANTHROPIC_API_KEY`` (or an ``ant`` profile)
    by default; pass ``api_key`` only when you must inject a specific key.
    """
    if api_key:
        return anthropic.Anthropic(api_key=api_key)
    return anthropic.Anthropic()


def chat_with_store_manager(
    user_message: str,
    *,
    client: anthropic.Anthropic | None = None,
    max_tokens: int = MAX_TOKENS,
) -> str:
    """Send a message to the MXD MDA Store Manager persona.

    Args:
        user_message: The operator or customer-facing request.
        client: Optional pre-built Anthropic client (handy for tests/reuse).
        max_tokens: Output token ceiling for the reply.

    Returns:
        The assistant's text response, or an error string on failure.

    Note:
        Creativity-vs-precision is steered through the system prompt and
        adaptive thinking rather than ``temperature`` — sampling parameters
        are not supported on Opus 4.8 and would raise a 400.

        When ``SHOPIFY_MCP_URL`` is set, the persona is given live Shopify
        tools via the MCP connector and may query (and, if writes are
        enabled, modify) the store while answering.
    """
    client = client or _client()
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_message}]
    mcp = _shopify_mcp_config()
    try:
        if mcp is not None:
            response = _run_with_shopify(client, messages, max_tokens, *mcp)
        else:
            response = client.messages.create(
                model=MODEL,
                max_tokens=max_tokens,
                system=STORE_MANAGER_SYSTEM_PROMPT,
                thinking={"type": "adaptive"},
                messages=messages,
            )
    except anthropic.APIError as exc:
        return f"An error occurred: {exc}"

    return _text(response)


def _run_with_shopify(
    client: anthropic.Anthropic,
    messages: list[dict[str, Any]],
    max_tokens: int,
    mcp_servers: list[dict[str, Any]],
    tools: list[dict[str, Any]],
    *,
    max_continuations: int = 5,
) -> anthropic.types.Message:
    """Call the API with the Shopify MCP connector attached.

    The connector executes MCP tools server-side. If the server-side loop hits
    its iteration limit it returns ``stop_reason == "pause_turn"``; re-send to
    resume, bounded by ``max_continuations``.
    """
    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=STORE_MANAGER_SYSTEM_PROMPT,
        thinking={"type": "adaptive"},
        mcp_servers=mcp_servers,
        tools=tools,
        betas=[MCP_BETA],
        messages=messages,
    )
    for _ in range(max_continuations):
        if response.stop_reason != "pause_turn":
            break
        messages = [*messages, {"role": "assistant", "content": response.content}]
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=STORE_MANAGER_SYSTEM_PROMPT,
            thinking={"type": "adaptive"},
            mcp_servers=mcp_servers,
            tools=tools,
            betas=[MCP_BETA],
            messages=messages,
        )
    return response


def _text(response: anthropic.types.Message) -> str:
    """Extract concatenated text blocks from a response (skips thinking/tools)."""
    return "\n".join(
        block.text for block in response.content if block.type == "text"
    ).strip()


def _main() -> None:
    """Initialize the persona and run a launch-readiness smoke prompt."""
    print("Initializing MXD MDA Store Manager...\n")
    print("-" * 50)

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY is not set; set it before running this demo.")
        return

    if _shopify_mcp_config() is not None:
        mode = "read+write" if _env_flag("SHOPIFY_ALLOW_WRITES") else "read-only"
        print(f"Shopify MCP: connected ({mode}).")
    else:
        print("Shopify MCP: not configured (set SHOPIFY_MCP_URL to enable).")

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
