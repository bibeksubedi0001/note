import re, os, sys

INPUT = r"D:\Final Year\Theory\cm\ocr_output\full_ocr_text.txt"
OUTDIR = r"D:\Final Year\Theory\cm\ocr_output"

with open(INPUT, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Build page index: page_num -> (start_line_idx, end_line_idx)
page_positions = []
for i, line in enumerate(lines):
    m = re.match(r"^PAGE (\d+)$", line.strip())
    if m:
        page_positions.append((int(m.group(1)), i))

# Print first 2 content lines of each page
print("=== Page content summary ===")
for idx, (pnum, line_idx) in enumerate(page_positions):
    cl = []
    for j in range(line_idx + 1, min(line_idx + 15, len(lines))):
        s = lines[j].strip()
        if s and s != "=" * 60 and "CamScanner" not in s:
            cl.append(s)
        if len(cl) >= 2:
            break
    print(f"P{pnum:3d}: {' | '.join(cl[:2])[:120]}")
