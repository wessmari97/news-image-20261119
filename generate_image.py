"""Draw the 19 November 2026 world-news poster, 1024x1024 PNG.

Run: python3 generate_image.py
Writes entry.png next to this file. Deterministic: fixed text, fixed
colours, fixed layout, no network, no timestamps, no randomness.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(draw, x, y, w, h, tag, tag_col, headline, body, head_size=30):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill="white",
                           outline="#D9DEE6", width=2)
    draw.rounded_rectangle([x, y, x + w, y + 34], radius=14, fill=tag_col)
    draw.rectangle([x, y + 20, x + w, y + 34], fill=tag_col)
    draw.text((x + 16, y + 7), tag, font=font(BOLD, 15), fill="white")
    fnt = font(BOLD, head_size)
    lines = wrap(draw, headline, fnt, w - 32)
    yy = y + 46
    for line in lines:
        draw.text((x + 16, yy), line, font=fnt, fill="#111827")
        yy += head_size + 6
    fnt2 = font(REG, 19)
    for line in wrap(draw, body, fnt2, w - 32):
        draw.text((x + 16, yy), line, font=fnt2, fill="#374151")
        yy += 25


def main():
    img = Image.new("RGB", (W, H), "#F3F4F6")
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 148], fill="#0F2040")
    d.rectangle([0, 148, W, 156], fill="#C8102E")
    d.text((32, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 54), fill="white")
    d.text((32, 96), "THURSDAY, 19 NOVEMBER 2026  •  WORLD NEWS IN ONE IMAGE",
           font=font(BOLD, 22), fill="#FBBF24")
    d.text((32, 124), "Six stories that defined the day, from The Hague to Shenzhen",
           font=font(REG, 18), fill="#CBD5E1")
    # Hero: ICJ ruling
    panel(d, 24, 176, 976, 196, "1  •  JUSTICE — THE HAGUE", "#7C3AED",
          "World Court: Myanmar committed genocide against the Rohingya",
          "The International Court of Justice ruled 9–6 — the first time the "
          "court has found a state guilty of genocide — over mass killings and "
          "sexual violence against the Rohingya in Rakhine State.", 32)
    # Row 2
    panel(d, 24, 392, 478, 218, "2  •  SUMMIT — SHENZHEN", "#0E7490",
          "Trump, Xi and Putin hold first three-way summit",
          "The three leaders met in Shenzhen and issued a joint peace "
          "declaration, pledging further talks on nuclear risks.", 27)
    panel(d, 522, 392, 478, 218, "3  •  UNREST — BANGLADESH", "#B91C1C",
          "Violence spreads across Bangladesh",
          "The interim leader's ancestral home was set on fire as unrest "
          "hit 28 districts across the country.", 27)
    # Row 3
    panel(d, 24, 630, 478, 218, "4  •  CLIMATE — ANTALYA", "#92400E",
          "COP31 ministers try to unblock talks",
          "Ministers met in informal session in Antalya to overcome "
          "differences and agree a final text.", 27)
    panel(d, 522, 630, 478, 218, "5  •  ENERGY — HORMUZ", "#166534",
          "Hormuz crisis threatens energy security",
          "Iran widened its Gulf attacks as the IEA called the crisis the "
          "greatest threat ever seen to energy security.", 27)
    # Bottom strip
    d.rounded_rectangle([24, 868, 1000, 972], radius=14, fill="#0F2040")
    d.text((44, 880), "ALSO ON 19 NOVEMBER", font=font(BOLD, 17), fill="#FBBF24")
    d.text((44, 908), "Senate rejects Iran war-powers resolution, 51–48  •  Anthropic prices IPO at $83",
           font=font(REG, 17), fill="white")
    d.text((44, 934), "Gaza: Israeli forces cross ceasefire line  •  Van Gogh sells for $190.4m, a record",
           font=font(REG, 17), fill="white")
    d.text((24, 984), "Drawn from reports published on 19 November 2026  •  make.fun — news-image-20261119",
           font=font(REG, 15), fill="#6B7280")
    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
