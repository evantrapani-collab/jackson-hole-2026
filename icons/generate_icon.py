#!/usr/bin/env python3
"""Generate the home-screen icon for the Trip HQ dashboard.

    python3 icons/generate_icon.py           # writes ../apple-touch-icon.png
    python3 icons/generate_icon.py --check   # verify the PNG matches this art

Why this exists: iOS *ignores* the SVG data-URI favicon in index.html when you
"Add to Home Screen". Safari looks for a real `apple-touch-icon` PNG, and with
none it falls back to a letter tile (the "J" of the app title). So the icon has
to be a checked-in raster file, and this script is its source of truth — edit
the ART section below and re-run rather than hand-editing the PNG.

No third-party deps on purpose (same rule as maps/generate_places.py): the
image is rasterized 4x and box-downsampled for antialiasing, then written with
a minimal PNG encoder from the standard library.

The icon is deliberately full-bleed and square with no rounded corners or
transparency: iOS applies its own squircle mask and composites black behind any
alpha. Nothing load-bearing sits near the corners, since the mask eats them.
"""

import argparse
import struct
import sys
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "apple-touch-icon.png"

SIZE = 180  # what iOS asks for; it downscales to 120/152/167 itself
SS = 4      # supersampling factor -> antialiasing
W = SIZE * SS
S = W / 100.0  # art units (0..100 square) -> supersampled pixels


def rgb(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))


# ---------------------------------------------------------------- ART -------
# Coordinates are in a 0..100 square, y pointing down. Palette matches the
# dashboard's CSS variables, with the ridges pushed apart in value so the three
# layers still read as three layers at 60 px on a phone.
SKY_TOP = rgb("#0a0f1a")
SKY_HORIZON = rgb("#2a3f66")
SKY_STOP = 62          # y where the gradient reaches SKY_HORIZON
MOON = rgb("#f5b942")  # --gold
SNOW = rgb("#eaf0fb")  # --ink
RIDGE_BACK = rgb("#3c5180")
RIDGE_MID = rgb("#24345a")
RIDGE_FRONT = rgb("#131c2e")

STARS = [(14, 18), (28, 30), (44, 12), (60, 24), (88, 14), (22, 44)]

# The Grand at (50,22), flanked by lower peaks — the same silhouette language as
# the hero <svg> in index.html, simplified for a tiny square.
RIDGE_BACK_PTS = [(0, 100), (0, 62), (18, 46), (30, 56), (50, 22),
                  (68, 52), (82, 38), (100, 58), (100, 100)]
RIDGE_MID_PTS = [(0, 100), (0, 76), (22, 60), (40, 74), (58, 58),
                 (78, 76), (100, 64), (100, 100)]
RIDGE_FRONT_PTS = [(0, 100), (0, 88), (25, 80), (50, 89), (75, 79),
                   (100, 87), (100, 100)]
SNOWCAPS = [[(50, 22), (41, 35), (59, 35)], [(82, 38), (76, 47), (88, 47)]]


def paint(canvas):
    """Draw the scene onto a W x W float RGB canvas, back to front."""
    for py in range(W):
        y = (py + 0.5) / S
        t = min(1.0, y / SKY_STOP)
        t = t * t * (3 - 2 * t)  # ease so the horizon glow isn't a flat ramp
        row = [SKY_TOP[c] + (SKY_HORIZON[c] - SKY_TOP[c]) * t for c in range(3)]
        base = py * W * 3
        for px in range(W):
            i = base + px * 3
            canvas[i], canvas[i + 1], canvas[i + 2] = row

    for x, y in STARS:
        circle(canvas, x, y, 0.7, SNOW, 0.7)
    circle(canvas, 72, 26, 9, MOON)

    polygon(canvas, RIDGE_BACK_PTS, RIDGE_BACK)
    for cap in SNOWCAPS:
        polygon(canvas, cap, SNOW)
    polygon(canvas, RIDGE_MID_PTS, RIDGE_MID)
    polygon(canvas, RIDGE_FRONT_PTS, RIDGE_FRONT)


# ------------------------------------------------------------ RASTERIZER ----
def blend(canvas, px, py, color, alpha):
    i = (py * W + px) * 3
    for c in range(3):
        canvas[i + c] += (color[c] - canvas[i + c]) * alpha


def span(canvas, py, x_from, x_to, color, alpha):
    px0 = max(0, int(x_from * S + 0.5))
    px1 = min(W - 1, int(x_to * S - 0.5))
    for px in range(px0, px1 + 1):
        blend(canvas, px, py, color, alpha)


def polygon(canvas, pts, color, alpha=1.0):
    ys = [p[1] for p in pts]
    y0 = max(0, int(min(ys) * S))
    y1 = min(W - 1, int(max(ys) * S) + 1)
    n = len(pts)
    for py in range(y0, y1 + 1):
        y = (py + 0.5) / S
        crossings = []
        for i in range(n):
            ax, ay = pts[i]
            bx, by = pts[(i + 1) % n]
            if (ay <= y < by) or (by <= y < ay):
                crossings.append(ax + (y - ay) * (bx - ax) / (by - ay))
        crossings.sort()
        for i in range(0, len(crossings) - 1, 2):
            span(canvas, py, crossings[i], crossings[i + 1], color, alpha)


def circle(canvas, cx, cy, r, color, alpha=1.0):
    y0 = max(0, int((cy - r) * S))
    y1 = min(W - 1, int((cy + r) * S) + 1)
    for py in range(y0, y1 + 1):
        dy = (py + 0.5) / S - cy
        if abs(dy) > r:
            continue
        dx = (r * r - dy * dy) ** 0.5
        span(canvas, py, cx - dx, cx + dx, color, alpha)


def downsample(canvas):
    """Average each SS x SS block -> the antialiased final image."""
    out = bytearray()
    scale = 1.0 / (SS * SS)
    for y in range(SIZE):
        out.append(0)  # PNG per-scanline filter byte: none
        rows = [(y * SS + sy) * W * 3 for sy in range(SS)]
        for x in range(SIZE):
            acc = [0.0, 0.0, 0.0]
            for row in rows:
                i = row + x * SS * 3
                for _ in range(SS):
                    acc[0] += canvas[i]
                    acc[1] += canvas[i + 1]
                    acc[2] += canvas[i + 2]
                    i += 3
            for c in acc:
                out.append(min(255, max(0, round(c * scale * 255))))
    return bytes(out)


def encode_png(raw):
    def chunk(tag, data):
        body = tag + data
        return (struct.pack(">I", len(data)) + body
                + struct.pack(">I", zlib.crc32(body) & 0xFFFFFFFF))

    header = struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0)  # 8-bit RGB
    return (b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(raw, 9))
            + chunk(b"IEND", b""))


def render():
    canvas = [0.0] * (W * W * 3)
    paint(canvas)
    return encode_png(downsample(canvas))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="verify the checked-in PNG matches, without rewriting")
    args = ap.parse_args()

    png = render()
    if args.check:
        current = OUT.read_bytes() if OUT.exists() else None
        if current != png:
            print(f"{OUT.name} is out of date — run: python3 icons/generate_icon.py")
            return 1
        print(f"{OUT.name} is up to date.")
        return 0

    OUT.write_bytes(png)
    print(f"Wrote {OUT} ({SIZE}x{SIZE}, {len(png):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
