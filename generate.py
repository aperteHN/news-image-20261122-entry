#!/usr/bin/env python3
"""One-page newspaper image summing up world news of Sunday 22 Nov 2026.

Deterministic: fixed layout, fixed text, no randomness, no timestamps.
Stories as reported on 22 Nov 2026 (AFP/AP and wire roundups that day):
COP31 collapse in Antalya; Russian strikes near Kyiv and Kryvyi Rih;
drone-hit ships in the Baltic and off Benghazi; Iran/Hormuz tanker strikes
and Bahrain Sitra plant; Khartoum drone strikes; UK-EU trade/travel deals;
Mexico cartel boss captured in Sinaloa; Brazil storm, Nigeria boat capsize,
Indonesia factory fire; France protests; Verstappen wins Las Vegas GP;
India declare 720/9 against New Zealand; West Bank settler arson.
Output: entry.png beside this file (1024x1024 PNG).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (18, 18, 20)
MUTED = (92, 88, 80)
RED = (178, 34, 40)
BLUE = (28, 74, 135)
TEAL = (16, 110, 105)
ORANGE = (199, 102, 18)
PURPLE = (94, 58, 140)
GREEN = (46, 110, 52)
BROWN = (130, 82, 30)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(x, y, text, font, color, maxw, leading):
    for line in wrap(text, font, maxw):
        d.text((x, y), line, font=font, fill=color)
        y += leading
    return y


# ---- Masthead ----
d.rectangle([0, 0, W, 148], fill=INK)
d.text((36, 18), "THE WORLD IN ONE DAY", font=f(SERIF_B, 54), fill=(255, 252, 244))
d.text((36, 88), "SUNDAY  \u2022  22 NOVEMBER 2026", font=f(SANS_B, 34), fill=(255, 196, 64))
d.text((716, 92), "GLOBAL NEWS", font=f(SANS_B, 28), fill=(210, 208, 200))
d.line([36, 160, W - 36, 160], fill=INK, width=3)

# ---- Lead story: COP31 ----
y = 174
d.rectangle([36, y, W - 36, y + 188], fill=(255, 255, 255), outline=INK, width=2)
d.rectangle([36, y, W - 36, y + 38], fill=RED)
d.text((52, y + 7), "LEAD  \u2022  CLIMATE  \u2022  ANTALYA, TURKEY", font=f(SANS_B, 23), fill=(255, 255, 255))
text_block(52, y + 46, "COP31 CLIMATE TALKS COLLAPSE WITHOUT A DEAL", f(SANS_B, 37), INK, W - 300, 44)
text_block(52, y + 136,
           "UN summit ends in record overtime; draft deal omits fossil fuels. "
           "EU & island nations reject it.",
           f(SANS, 21), MUTED, W - 300, 25)
# simple globe motif, right side of lead panel
cx, cy, r = 905, y + 100, 44
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=BLUE, width=4)
d.ellipse([cx - 20, cy - r, cx + 20, cy + r], outline=BLUE, width=3)
d.line([cx - r, cy, cx + r, cy], fill=BLUE, width=3)
d.line([cx - r + 8, cy - 30, cx + r - 8, cy - 30], fill=BLUE, width=2)
d.line([cx - r + 8, cy + 30, cx + r - 8, cy + 30], fill=BLUE, width=2)
d.text((cx - 34, cy + r + 5), "NO DEAL", font=f(SANS_B, 18), fill=RED)

# ---- Six panels, 2 columns x 3 rows ----
panels = [
    ("UKRAINE WAR", BLUE,
     "Strikes kill near Kyiv; ships ablaze",
     "Russian attack near Kyiv kills 3, buries others; missiles kill 2 in "
     "Kryvyi Rih. Drone-hit ships burn in Baltic & off Libya."),
    ("MIDDLE EAST  \u2022  HORMUZ", ORANGE,
     "Iran hits tankers; Bahrain plant struck",
     "Tankers struck near Strait of Hormuz. Bahrain: Iranian attack sets Sitra "
     "plant ablaze, wounds 2. Tehran shows \u201cmissile city.\u201d"),
    ("SUDAN", PURPLE,
     "Drones strike homes & UN in Khartoum",
     "Drone strikes hit homes and a UN building in Sudan's capital, "
     "witnesses and the UN said Sunday."),
    ("UK  \u2013  EU RESET", TEAL,
     "Britain & EU strike trade, travel deals",
     "London & Brussels agree trade and travel deals, pledging to rebuild "
     "ties a decade after Brexit."),
    ("MEXICO", GREEN,
     "Cartel boss captured; 11 dead",
     "Fausto Isidro Meza Flores, \u201cEl Chapo Isidro,\u201d captured in "
     "Sinaloa after a bloody firefight that left at least 11 dead."),
    ("DISASTERS", BROWN,
     "Storm, boat & factory fire tolls rise",
     "Brazil storm kills 4, injures 162. Nigeria funeral boat: 24 dead. "
     "Indonesia: search after factory fire."),
]
px, py = 36, 374
pw, ph, gap = 470, 168, 10
for i, (kicker, color, head, body) in enumerate(panels):
    x = px + (i % 2) * (pw + gap)
    yy = py + (i // 2) * (ph + gap)
    d.rectangle([x, yy, x + pw, yy + ph], fill=(255, 255, 255), outline=(190, 185, 172), width=2)
    d.rectangle([x, yy, x + pw, yy + 32], fill=color)
    d.text((x + 14, yy + 5), kicker, font=f(SANS_B, 20), fill=(255, 255, 255))
    text_block(x + 14, yy + 40, head, f(SANS_B, 25), INK, pw - 28, 30)
    text_block(x + 14, yy + 100, body, f(SANS, 18), MUTED, pw - 28, 22)

# ---- Bottom ticker ----
ty = py + 3 * (ph + gap) + 4
d.rectangle([36, ty, W - 36, H - 24], fill=INK)
text_block(52, ty + 9,
           "ALSO: Verstappen wins Las Vegas GP  \u2022  India declare 720/9 vs "
           "New Zealand  \u2022  France marches, 6th weekend, over living costs  \u2022  "
           "West Bank settlers torch homes",
           f(SANS_B, 19), (255, 240, 200), W - 104, 23)

import os
img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"),
         format="PNG", optimize=True)
print("saved")
