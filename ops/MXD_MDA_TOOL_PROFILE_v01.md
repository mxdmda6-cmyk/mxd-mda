# MXD_MDA_TOOL_PROFILE_v01

Status Date: 2026-06-15 / Central Time
Owner: MXD-MDA
Purpose: define connected production tools, test status, setup actions completed, and human-only account gates.

## Decision
Ship Gate Clearance is active. The connected stack can support storefront operations, print-on-demand setup, project documentation, file discovery, inbox/calendar checks, and repository documentation. KDP banking remediation remains human-in-browser only because no KDP connector is available in this session.

## Tested Tools

| Tool | Status | Result | Notes |
|---|---|---|---|
| Gmail | Tested | Connected | Search did not surface a clean KDP PSP notice in the connected inbox. |
| Shopify | Tested + Mutated | Connected | Store verified. Smart collection created: MXD-MDA Print-on-Demand. |
| Printify | Tested + Generated | Connected | Generated Crow Codex / Find Crow artwork and applied it to the fixed product catalog. |
| Google Drive | Tested | Connected | Account profile confirmed and MXD-MDA project files found. |
| Google Calendar | Tested | Connected | No events found for the June 15-22, 2026 window. |
| Google Contacts | Tested | Connected | Search for Angela returned no matching contact. |
| Dropbox | Tested | Connected | Account identity verified. No file mutations performed. |
| Box | Tested | Connected | Account active. No file mutations performed. |
| Airtable | Tested | Connected | Bases visible, including Centralized Project Management and MXD-MDA Analytics. No data mutations performed. |
| GitHub | Tested + Mutated | Connected | Repo verified; this profile created in ops. |
| Notion | Partial | Tool available | Notion markdown spec resource fetch failed, so Notion page creation was deferred. |
| Web | Tested | Connected | Official KDP PSP documentation verified. |

## Shopify / Printify Setup Log

### Shopify Collection Created
- Title: MXD-MDA Print-on-Demand
- Type: Smart collection
- Handle: mxd-mda-print-on-demand
- Rule logic: product matches any of these: tag is Printify, tag is POD, or vendor is Printify.
- Product count at creation: 0
- Purpose: keep physical POD products separate from digital downloads.

### Printify Product Set Generated
- Artwork theme: MXD-MDA Crow Codex ritual seal
- Phrase: "Find Crow. Find Yourself."
- Visual lane: gothic-noir, oil-paint realism texture, indigo/bone/gold contrast, silhouette Crow, alchemical fragments, controlled mystery.
- Product catalog returned:
  - Unisex Heavy Blend Hooded Sweatshirt
  - Unisex Garment-Dyed T-shirt
  - Unisex Heavy Cotton Tee
  - Cotton Canvas Tote Bag
- Generated image dimensions: 1024 x 1024
- Generated image ID: 6a30cb52a68da461dec397db

## KDP Banking Compliance Gate

### Current State
- No KDP connector is available.
- Inbox search did not find a clean KDP PSP notice.
- KDP Getting Paid remains the source of truth for account-specific flags.

### Human-Only Action
Log into KDP, open Account, then Getting Paid. Capture only non-sensitive status lines, institution names, currency/marketplace, and visible error categories.

### Required Diagnosis Fields
For each payment entry, record:
- Marketplace/currency
- Institution or PSP name only
- Public-facing account holder/entity label shown
- KDP status message
- Error category: non-participating PSP, pending KYC, deposit-taking-bank-only, or no error
- Whether Save produces green confirmation

## Operating Rules

1. Public metadata must not include private addresses, medical/housing/legal details, family names, old residences, account numbers, government IDs, or verification documents.
2. KDP banking changes must be completed by the account holder in the browser.
3. Printify/Shopify physical products remain draft or QA until mockups, shipping profiles, pricing, and fulfillment settings are verified.
4. Digital products and physical POD products stay separated by collection, tags, product type, and fulfillment logic.
5. No product goes live without visual QA: no watermarks, no UI artifacts, no unreadable text, no broken mockups.

## Risks

- KDP royalties and publishing can be blocked if the payment account gate is unresolved.
- Printify generation is not the same as confirmed Shopify publish/sync; verify both sides before launch.
- Smart collection waits for products tagged Printify or POD or vendor Printify.
- Notion write path needs re-test because the markdown spec resource fetch failed.

## Next 3 Moves

1. KDP: complete Getting Paid diagnosis and capture safe screenshots/status text only.
2. Printify/Shopify: verify whether generated Printify products are pushed to Shopify; tag synced products with Printify and POD.
3. QA: keep all physical products unpublished until mockups, shipping, pricing, and fulfillment flow pass review.
