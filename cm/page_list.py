"""
Scan full_ocr_text.txt to find chapter boundaries and split into chapter files.
Strategy: Look at the first few content lines after each PAGE marker to detect chapter title pages.
"""
import re, os

INPUT = r"D:\Final Year\Theory\cm\ocr_output\full_ocr_text.txt"
OUTDIR = r"D:\Final Year\Theory\cm\ocr_output"

with open(INPUT, "r", encoding="utf-8") as f:
    full_text = f.read()
lines = full_text.split("\n")

# Build page index
pages = []  # list of (page_num, line_start_idx)
for i, line in enumerate(lines):
    m = re.match(r"^PAGE (\d+)$", line.strip())
    if m:
        pages.append((int(m.group(1)), i))

print(f"Total lines: {len(lines)}, Total pages: {len(pages)}")

# For each page, extract the first ~5 meaningful content lines
def get_page_content(page_idx, num_lines=5):
    _, start = pages[page_idx]
    cl = []
    for j in range(start + 1, min(start + 30, len(lines))):
        s = lines[j].strip()
        if s and s != "=" * 60 and "CamScanner" not in s:
            cl.append(s)
        if len(cl) >= num_lines:
            break
    return cl

# Print condensed listing
for pi, (pnum, lidx) in enumerate(pages):
    cl = get_page_content(pi, 2)
    summary = " | ".join(cl)[:120]
    print(f"P{pnum:3d}: {summary}")
