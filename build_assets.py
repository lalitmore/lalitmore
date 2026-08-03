#!/usr/bin/env python3
"""
Minimal profile — single banner SVG generator.
One asset, one animation (a blinking caret). Warm charcoal + honey accent.
All animation is SMIL so it survives GitHub's image proxy. No scripts, no webfonts.
Re-run after editing:  python3 build_assets.py
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)

# ---- palette (warm + welcoming, single accent) ------------------------------
BG     = "#100D0A"   # warm charcoal
BORDER = "#241E18"   # warm hairline
TXT    = "#F3ECE3"   # warm off-white
MUT    = "#A79C8F"   # warm gray
MUT2   = "#6E655B"   # dim warm gray
ACCENT = "#F2A65A"   # honey amber

SANS = "'Segoe UI',system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular','JetBrains Mono',Menlo,Consolas,monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build_banner():
    W, H = 1000, 210
    role = "AI / full-stack engineer \u00b7 multi-agent systems"
    sub = "B.S. Computer Science + Data Science \u00b7 Pitt Honors '27 \u00b7 GCP Associate Cloud Engineer"

    x0 = 56
    char_w = 8.35            # approx mono width at 14px
    caret_x = x0 + len(role) * char_w + 6

    b = []
    b.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="16" fill="{BG}"/>')
    b.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="15.5" '
             f'fill="none" stroke="{BORDER}" stroke-width="1"/>')

    # name
    b.append(f'<text x="{x0-2}" y="92" font-family="{SANS}" font-size="46" '
             f'font-weight="600" fill="{TXT}" letter-spacing="0.5">Lalit More</text>')
    # static warm signature rule under the name
    b.append(f'<rect x="{x0-2}" y="108" width="66" height="3" rx="1.5" fill="{ACCENT}"/>')

    # role line + the one animation (blinking caret)
    b.append(f'<text x="{x0}" y="146" font-family="{MONO}" font-size="14" '
             f'fill="{MUT}">{esc(role)}</text>')
    b.append(f'<rect x="{caret_x:.0f}" y="133" width="8" height="17" fill="{ACCENT}">'
             f'<animate attributeName="opacity" values="1;0" dur="0.55s" '
             f'calcMode="discrete" repeatCount="indefinite"/></rect>')

    # credentials subline
    b.append(f'<text x="{x0}" y="178" font-family="{MONO}" font-size="12" '
             f'fill="{MUT2}">{esc(sub)}</text>')

    svg = (f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'preserveAspectRatio="xMidYMid meet" role="img" '
           f'xmlns="http://www.w3.org/2000/svg">'
           f'<title>Lalit More \u2014 AI / full-stack engineer</title>'
           f'{"".join(b)}</svg>')
    path = os.path.join(OUT, "banner.svg")
    with open(path, "w") as f:
        f.write(svg)
    return len(svg)


if __name__ == "__main__":
    n = build_banner()
    print("wrote assets/banner.svg", n, "bytes")
