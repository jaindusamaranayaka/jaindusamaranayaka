#!/usr/bin/env python3
"""
Render a terminal neofetch-style info card SVG (840 x 880) that sits beside jaindu-ascii.svg.
Pixel-perfect alignment with two-column layout, high-legibility typography,
robust SMIL + CSS fade-in animations, and classic Neofetch ANSI color blocks.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "info-card.svg")

# Load live stats if available
stats_summary = "90 Contributions · 3d Streak"
if os.path.exists(DATA_PATH):
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            d = json.load(f)
            tot = d.get("total_contributions", 0)
            ls = d.get("longest_streak", {}).get("length", 0)
            stats_summary = f"{tot:,} Contributions · {ls}d Peak Streak"
    except Exception:
        pass

W, H = 840, 880
PAD = 28
TITLEBAR_H = 32

BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
CYAN = "#38bdf8"
GREEN = "#39d353"
YELLOW = "#facc15"
PURPLE = "#c084fc"
ORANGE = "#fb923c"
BLUE = "#60a5fa"

# (Key, Value, KeyColor)
fields = [
    ("OS", "Ubuntu 24.04 LTS / Arch Linux (x86_64)", CYAN),
    ("Host", "University of Moratuwa [ENTC Department]", GREEN),
    ("Role", "Hardware & Embedded Systems Engineer", INK),
    ("Degree", "B.Sc. Eng (Hons) Electronic & Telecom", YELLOW),
    ("Silicon / EDA", "SystemVerilog · Yosys · OpenROAD · KLayout", ORANGE),
    ("FPGA & CAD", "Intel Quartus Prime · Altium · SolidWorks", PURPLE),
    ("Software & ML", "Python · C++ · TensorFlow · OpenCV · Docker", BLUE),
    ("RISC CPU", "16-bit Pipelined RISC CPU (ASIC Tapeout Flow)", GREEN),
    ("Accelerators", "FPGA CNN Hardware Matrix / Multiplier Cores", CYAN),
    ("Robotics & IoT", "Multi-Axis Robotic Arm · ESP32 Telemetry", INK),
    ("Activity", stats_summary, GREEN),
    ("Portfolio", "jaindusamaranayaka.github.io/portfolio", CYAN),
]

KEY_X = PAD + 12
COLON_X = KEY_X + 175
VAL_X = COLON_X + 18

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<style>',
    '.row { animation: fadeIn 0.35s ease-out both; }',
    '@keyframes fadeIn { 0% { opacity: 0; transform: translateY(8px); } 100% { opacity: 1; transform: translateY(0); } }',
    '@media (prefers-reduced-motion: reduce) { .row { opacity: 1 !important; transform: none !important; animation: none !important; } }',
    '</style>',
    '<defs>',
    f'<linearGradient id="cardbg" x1="0" y1="0" x2="0" y2="1">',
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/>',
    '</linearGradient>',
    '</defs>',
    # Background and border
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#cardbg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

# Title bar dots
for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*18}" cy="{TITLEBAR_H/2}" r="5.5" fill="{dot}"/>')

parts.append(
    f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4.5}" fill="{MUTED}" font-size="13" font-weight="600" text-anchor="middle">'
    f'jaindu@moratuwa: ~$ neofetch --profile</text>'
)

# Header inside terminal
start_y = TITLEBAR_H + 48
parts.append(
    f'<g class="row" style="animation-delay: 0.05s">'
    f'<text x="{KEY_X}" y="{start_y}" font-size="26" font-weight="700" fill="{CYAN}">jaindu<tspan fill="{MUTED}">@</tspan><tspan fill="{GREEN}">moratuwa</tspan></text>'
    f'<text x="{KEY_X}" y="{start_y + 18}" font-size="16" fill="{MUTED}">----------------------------------------------------------------</text>'
    f'</g>'
)

curr_y = start_y + 58
line_height = 46

for idx, (k, v, col) in enumerate(fields):
    delay = 0.1 + idx * 0.08
    parts.append(
        f'<g class="row" style="animation-delay: {delay:.2f}s">'
        f'<text x="{KEY_X}" y="{curr_y}" font-size="20" font-weight="700" fill="{col}">{k}</text>'
        f'<text x="{COLON_X}" y="{curr_y}" font-size="20" font-weight="600" fill="{MUTED}">:</text>'
        f'<text x="{VAL_X}" y="{curr_y}" font-size="20" font-weight="400" fill="{INK}">{v}</text>'
        f'</g>'
    )
    curr_y += line_height

# Memory bar / system status
bar_y = curr_y + 14
parts.append(
    f'<g class="row" style="animation-delay: 1.1s">'
    f'<text x="{KEY_X}" y="{bar_y}" font-size="15" fill="{MUTED}">Silicon Load  : '
    f'<tspan fill="{GREEN}">[||||||||||||||||||||||||||||||||||||||||]</tspan> '
    f'<tspan fill="{INK}">16-Core RISC CPU / 100% Neural Accel</tspan></text>'
    f'</g>'
)

# Classic 16-color Neofetch ANSI blocks
palette_y = bar_y + 32
block_w = 42
block_h = 22
colors_dark = ["#161b22", "#f85149", "#56d364", "#e3b341", "#58a6ff", "#bc8cff", "#39c5cf", "#b1bac4"]
colors_bright = ["#484f58", "#ff7b72", "#7ee787", "#f2cc60", "#79c0ff", "#d2a8ff", "#56d4dd", "#f0f6fc"]

parts.append(f'<g class="row" style="animation-delay: 1.25s">')
for i, col in enumerate(colors_dark):
    bx = KEY_X + i * (block_w + 6)
    parts.append(f'<rect x="{bx}" y="{palette_y}" width="{block_w}" height="{block_h}" rx="3" fill="{col}"/>')

for i, col in enumerate(colors_bright):
    bx = KEY_X + i * (block_w + 6)
    parts.append(f'<rect x="{bx}" y="{palette_y + block_h + 4}" width="{block_w}" height="{block_h}" rx="3" fill="{col}"/>')

parts.append('</g>')
parts.append('</svg>')

svg = "".join(parts)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"wrote {OUT}: {W} x {H}, {len(svg)//1024} KB")
