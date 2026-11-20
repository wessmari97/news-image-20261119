"""Render the 19 November 2026 world-news poster as a 1024x1024 PNG.

The poster is data-driven: STORIES holds the day's six stories, and the
renderer lays them out as a front page. Run it with:

    python3 generate_image.py

It writes entry.png in this directory. The output is deterministic:
fixed stories, fixed palette, fixed geometry, no network access,
no clock, no randomness.
"""
from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
NAVY = (15, 32, 64)
INK = (17, 24, 39)
GREY = (55, 65, 81)
FAINT = (107, 114, 128)
PAPER = (243, 244, 246)
GOLD = (251, 191, 36)
RED = (200, 16, 46)
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_PLAIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

STORIES = [
    {
        "kicker": "1  •  JUSTICE — THE HAGUE",
        "colour": (124, 58, 237),
        "title": "World Court: Myanmar committed genocide against the Rohingya",
        "text": "The International Court of Justice ruled 9–6 — the first time the "
                "court has found a state guilty of genocide — over mass killings and "
                "sexual violence against the Rohingya in Rakhine State.",
        "big": True,
    },
    {
        "kicker": "2  •  SUMMIT — SHENZHEN",
        "colour": (14, 116, 144),
        "title": "Trump, Xi and Putin hold first three-way summit",
        "text": "The three leaders met in Shenzhen and issued a joint peace "
                "declaration, pledging further talks on nuclear risks.",
        "big": False,
    },
    {
        "kicker": "3  •  UNREST — BANGLADESH",
        "colour": (185, 28, 28),
        "title": "Violence spreads across Bangladesh",
        "text": "The interim leader's ancestral home was set on fire as unrest "
                "hit 28 districts across the country.",
        "big": False,
    },
    {
        "kicker": "4  •  CLIMATE — ANTALYA",
        "colour": (146, 64, 14),
        "title": "COP31 ministers try to unblock talks",
        "text": "Ministers met in informal session in Antalya to overcome "
                "differences and agree a final text.",
        "big": False,
    },
    {
        "kicker": "5  •  ENERGY — HORMUZ",
        "colour": (22, 101, 52),
        "title": "Hormuz crisis threatens energy security",
        "text": "Iran widened its Gulf attacks as the IEA called the crisis the "
                "greatest threat ever seen to energy security.",
        "big": False,
    },
]

ALSO = [
    "Senate rejects Iran war-powers resolution, 51–48  •  Anthropic prices IPO at $83",
    "Gaza: Israeli forces cross ceasefire line  •  Van Gogh sells for $190.4m, a record",
]


def load(size, bold=True):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_PLAIN, size)


def flow(draw, text, face, width):
    """Split text into lines that fit width, in the given font."""
    out, current = [], ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if draw.textlength(candidate, font=face) <= width:
            current = candidate
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def card(draw, story, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill="white",
                           outline=(217, 222, 230), width=2)
    draw.rounded_rectangle([x, y, x + w, y + 34], radius=14, fill=story["colour"])
    draw.rectangle([x, y + 20, x + w, y + 34], fill=story["colour"])
    draw.text((x + 16, y + 7), story["kicker"], font=load(15), fill="white")
    size = 32 if story["big"] else 27
    title_face = load(size)
    cursor = y + 46
    for line in flow(draw, story["title"], title_face, w - 32):
        draw.text((x + 16, cursor), line, font=title_face, fill=INK)
        cursor += size + 6
    body_face = load(19, bold=False)
    for line in flow(draw, story["text"], body_face, w - 32):
        draw.text((x + 16, cursor), line, font=body_face, fill=GREY)
        cursor += 25


def header(draw):
    draw.rectangle([0, 0, CANVAS[0], 148], fill=NAVY)
    draw.rectangle([0, 148, CANVAS[0], 156], fill=RED)
    draw.text((32, 22), "THE WORLD IN ONE DAY", font=load(54), fill="white")
    draw.text((32, 96), "THURSDAY, 19 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE",
              font=load(22), fill=GOLD)
    draw.text((32, 124), "Six stories that defined the day, from The Hague to Shenzhen",
              font=load(18, bold=False), fill=(203, 213, 225))


def footer(draw):
    draw.rounded_rectangle([24, 868, 1000, 972], radius=14, fill=NAVY)
    draw.text((44, 880), "ALSO ON 19 NOVEMBER", font=load(17), fill=GOLD)
    for i, line in enumerate(ALSO):
        draw.text((44, 908 + i * 26), line, font=load(17, bold=False), fill="white")
    draw.text((24, 984), "Drawn from reports published on 19 November 2026  •  make.fun — news-image-20261119",
              font=load(15, bold=False), fill=FAINT)


def render():
    image = Image.new("RGB", CANVAS, PAPER)
    draw = ImageDraw.Draw(image)
    header(draw)
    lead = STORIES[0]
    card(draw, lead, 24, 176, 976, 196)
    for i, story in enumerate(STORIES[1:]):
        col = i % 2
        row = i // 2
        card(draw, story, 24 + col * 498, 392 + row * 238, 478, 218)
    footer(draw)
    image.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    render()
