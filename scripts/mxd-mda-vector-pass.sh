#!/usr/bin/env bash
set -euo pipefail

# MXD-MDA Vector Pass (slice -> masks -> optional SVG trace)
# Input:
#   Place ONE image here: assets/raster/source_table.png
# Output:
#   out/cells_png/*.png
#   out/cells_mask/*_mask.png
#   out/svg/*.svg   (only if potrace is installed)

mkdir -p assets/raster out/cells_png out/cells_mask out/svg

python - <<'PY'
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

src = Path("assets/raster/source_table.png")
if not src.exists():
    raise SystemExit("Missing assets/raster/source_table.png (put your table image there).")

img = Image.open(src).convert("RGBA")
w, h = img.size

# Heuristic crop window for the 1024x1536 table image we’re using.
# If you swap images later, adjust y0/y1.
y0, y1 = 240, 1480
grid = img.crop((0, y0, w, y1))

cols, rows = 3, 4
gw, gh = grid.size
cell_w = gw // cols
cell_h = gh // rows

out_png = Path("out/cells_png")
out_mask = Path("out/cells_mask")
out_png.mkdir(parents=True, exist_ok=True)
out_mask.mkdir(parents=True, exist_ok=True)

def make_mask(im):
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = g.filter(ImageFilter.GaussianBlur(0.6))
    g = g.filter(ImageFilter.UnsharpMask(2, 180, 3))
    bw = g.point(lambda p: 255 if p > 180 else 0).convert("1")
    return bw

for r in range(rows):
    for c in range(cols):
        left = c * cell_w
        upper = r * cell_h
        right = (c + 1) * cell_w if c < cols - 1 else gw
        lower = (r + 1) * cell_h if r < rows - 1 else gh

        cell = grid.crop((left, upper, right, lower))
        idx = r * cols + c + 1

        png_path = out_png / f"cell_{idx:02d}.png"
        cell.save(png_path)

        mask = make_mask(cell)
        mask_path = out_mask / f"cell_{idx:02d}_mask.png"
        mask.save(mask_path)

print("Done: sliced PNG cells + created masks.")
PY

# Optional: auto-trace masks into SVGs (best if potrace exists)
if command -v potrace >/dev/null 2>&1; then
  echo "potrace detected: generating SVGs..."
  for f in out/cells_mask/*_mask.png; do
    base="$(basename "$f" _mask.png)"
    potrace "$f" -s -o "out/svg/${base}.svg"
  done
  echo "Done: out/svg/*.svg created."
else
  echo "potrace not found. No problem:"
  echo "Use Inkscape: File > Import mask PNG > Path > Trace Bitmap > Save as SVG."
fi
