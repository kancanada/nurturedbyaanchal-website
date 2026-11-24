"""Draws a branded cover image for each recipe that has no real photo yet.
Run from repo root: python3 _tools/recipe_cards.py  (build.py calls it automatically)
Replace with Aanchal's own food photo by setting "image" on the recipe in content.py.
"""
import os, textwrap
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/google-fonts"
W, H = 1200, 900
CREAM = (250, 247, 240)


def font(weight, size):
    for name in (f"Poppins-{weight}.ttf", "Poppins-Bold.ttf"):
        p = os.path.join(FONT_DIR, name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def card(r, out):
    base = hex2rgb(r.get("colour", "#666640"))
    im = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(im)
    # bowl: plate rim + food + garnish
    cx, cy, R = 930, 560, 300
    d.ellipse((cx - R - 30, cy - R - 30, cx + R + 30, cy + R + 30), fill=(255, 255, 255))
    d.ellipse((cx - R, cy - R, cx + R, cy + R), fill=mix(base, (255, 255, 255), .15))
    d.ellipse((cx - R + 40, cy - R + 40, cx + R - 40, cy + R - 40), fill=base)
    for (dx, dy, s) in [(-90, -60, 26), (60, -110, 20), (110, 40, 24), (-30, 90, 22), (-150, 50, 18), (20, 0, 16)]:
        d.ellipse((cx + dx - s, cy + dy - s, cx + dx + s, cy + dy + s), fill=(102, 140, 60))
    d.ellipse((cx + 150 - 30, cy - 160 - 30, cx + 150 + 30, cy - 160 + 30), fill=mix(base, (255, 255, 255), .55))
    # text block
    d.text((70, 90), r.get("cat", "Recipe").upper(), font=font("Medium", 30), fill=(102, 102, 64))
    title = textwrap.fill(r["title"], 13)
    d.multiline_text((70, 150), title, font=font("SemiBold", 60), fill=(20, 20, 20), spacing=8)
    d.text((70, H - 150), f'{r["prep"] + r["cook"]} min  ·  serves {r["servings"]}', font=font("Regular", 34), fill=(70, 70, 70))
    d.text((70, H - 95), "nurturedbyaanchal.com", font=font("Medium", 30), fill=(95, 122, 139))
    im.save(out, quality=86, optimize=True, progressive=True)


def make_all(recipes):
    os.makedirs("images/recipes", exist_ok=True)
    for r in recipes:
        if r.get("image"):
            continue
        out = f'images/recipes/{r["slug"]}.jpg'
        card(r, out)
        r["image"] = "/" + out


if __name__ == "__main__":
    import sys
    sys.path.insert(0, "_tools")
    from content import RECIPES
    make_all(RECIPES)
    print("cards:", len(RECIPES))
