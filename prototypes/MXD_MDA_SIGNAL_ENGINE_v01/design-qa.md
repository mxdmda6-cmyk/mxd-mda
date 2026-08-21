# MXD-MDA Signal Engine — Design QA

- Source visual truth: `/workspace/scratch/6a59dcf569a1/generated_images/exec-4a63897e-c43d-45f5-b929-bca5759bec35.png`
- Implementation screenshot: `/workspace/scratch/6a59dcf569a1/MXD_MDA_SIGNAL_ENGINE_v01/qa/implementation-desktop-v03.jpg`
- Same-input comparison: `/workspace/scratch/6a59dcf569a1/MXD_MDA_SIGNAL_ENGINE_v01/qa/source-vs-implementation-v01.jpg`
- Browser URL: `http://terminal.local:4173/`
- CSS viewport: `1363 × 936`
- Source pixels: `1488 × 1057`
- Implementation pixels: `1348 × 926`, browser viewport capture at density 1
- Normalization: both source and implementation resized to 720 px high and joined horizontally for direct comparison
- State: desktop, dark, `SILENCE / CHAOS`, resolved signal, offer sheet closed

## Full-view comparison

The implementation preserves the source composition: opposing bone and indigo deckled sheets, a crimson torn seam, vertical tension words, fine antique-gold intersection geometry, centered poetic signal, restrained metadata, hard-edged gold action, and the single dry Crow note. The generated production assets retain genuine transparency and remain sharp at the rendered size.

The live product intentionally adds a narrow identity bar and tension selector above the composition. This is an accepted product constraint: it makes the reusable engine discoverable and navigable without turning the screen into a dashboard. The source's signal sits inside the intersection mark; the implementation gives it a little more vertical separation to improve reading and protect the conversion button at the browser's shorter viewport.

## Focused-region comparison

The central seam and conversion cluster were inspected at full screenshot scale. The font family, uppercase rhythm, button geometry, signal line breaks, metadata spacing, and contrast remain readable. Separate focused crops were not required because all critical text and assets are legible in the normalized comparison.

## Required fidelity surfaces

- Fonts and typography: Cormorant Garamond, Epilogue, and JetBrains Mono match the literary display, modern interface, and technical metadata roles in the source. Weights, spacing, and hierarchy are coherent; no clipping or truncation observed.
- Spacing and layout rhythm: opposing fragments preserve the source's asymmetry and meet toward a narrow center. The brand and selector rows add 114 px of intentional product chrome. Primary action and metadata retain clear separation.
- Colors and tokens: obsidian, dark indigo, bone, antique gold, crimson, and muted silver are consistently tokenized. Text and controls retain readable contrast.
- Image quality and asset fidelity: bone fragment, indigo fragment, and seam mark are dedicated RGBA assets generated from the selected source direction. No placeholders, CSS drawings, handcrafted SVGs, or emoji substitutes remain.
- Copy and content: primary source copy is preserved exactly. Alternate tension signals and offer copy stay within MXD-MDA voice. Public creator credit correctly uses Hue Moore.

## Interaction evidence

- Changed the tension from `SILENCE / CHAOS` to `MEMORY / IDENTITY`.
- Resolved the new signal through `BRING INTO CONTACT`.
- Opened `KEEP THIS FRAGMENT` and verified all three price editions.
- Selected the recommended `$79` edition.
- Entered a non-personal test address and completed the local proof reservation.
- Verified the success state and returned to the signal.
- Checked browser logs. No app-origin console errors were present; only unrelated browser-extension metadata errors appeared.

## Findings

- No P0, P1, or P2 issues remain.
- [P3] The identity and tension-selector rows make the implementation slightly denser than the source mock. Accepted because they enable the core repeated-use workflow.
- [P3] Cloud-browser captures visibly include the browser cursor in some frames. This is a capture artifact and must not be used as promotional artwork.

## Comparison history

- Initial implementation review: verified the resolved signal, three-offer sheet, local reservation, and success state. No blocking design differences found.
- Normalization pass: returned to `SILENCE / CHAOS`, matched the resolved state, captured at the same dark theme, and created a same-input comparison at equal height.
- Post-normalization evidence: tactile asset fidelity, typographic hierarchy, palette, copy, and conversion affordance remained intact.

## Follow-up polish

- Capture a clean cursor-free promotional image after launch packaging.
- Run one dedicated 390 px mobile visual capture when the browser surface supports viewport switching.

final result: passed
