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

Requires the ``ANTHROPIC_API_KEY`` environment variable (resolved by the SDK).
"""

from __future__ import annotations

import os

import anthropic

# Default to the most capable Opus-tier model. The retired
# claude-3-5-sonnet-20241022 (sunset 2025-10-28) is intentionally not used.
MODEL = "claude-opus-4-8"
MAX_TOKENS = 4096

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

    # content is a list of blocks (thinking, text, ...); keep only text.
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
