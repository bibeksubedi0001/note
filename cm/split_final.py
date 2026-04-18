"""
Split full_ocr_text.txt into chapter files using identified page boundaries.
"""
import re, os

INPUT = r"D:\Final Year\Theory\cm\ocr_output\full_ocr_text.txt"
OUTDIR = r"D:\Final Year\Theory\cm\ocr_output"

with open(INPUT, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Build page index: page_num -> line_index of the PAGE marker
page_line = {}
for i, line in enumerate(lines):
    m = re.match(r"^PAGE (\d+)$", line.strip())
    if m:
        page_line[int(m.group(1))] = i

# Chapter definitions: (chapter_num, title, start_page, end_page_exclusive)
# end_page is the first page of the NEXT chapter
chapters = [
    (0,  "Front Matter",                             1,    7),
    (1,  "Construction Management Framework",        7,   28),
    (2,  "Planning and Scheduling",                 28,   69),
    (3,  "Material Management",                     69,   98),
    (4,  "Equipment Management",                    98,  123),
    (5,  "Contract Management",                    123,  167),
    (6,  "Construction Process",                   167,  179),
    (7,  "Controlling Project Integration and Work",179, 216),
    (8,  "Site Management",                        216,  226),
    (9,  "Project Maintenance",                    226,  235),
    (10, "Personnel Organization and Management",  235,  273),
    (11, "Safety Management",                      273,  303),
    (12, "Specifications",                         303,  318),
    (13, "Valuation",                              318,  337),
    (14, "Annexes and Past Questions",             337,  387),  # 386+1
]

print(f"Total lines: {len(lines)}, Total pages: {len(page_line)}")
print(f"\n{'='*60}")
print(f"{'Ch':>3} {'Title':<45} {'Pages':>10} {'Lines':>8} {'Chars':>8}")
print(f"{'='*60}")

# Delete old chapter files first
for f in os.listdir(OUTDIR):
    if f.startswith("chapter") and f.endswith(".txt"):
        os.remove(os.path.join(OUTDIR, f))
    if f == "00_frontmatter.txt":
        os.remove(os.path.join(OUTDIR, f))

for ch_num, title, start_pg, end_pg in chapters:
    # Get line range
    if start_pg in page_line:
        # Go 2 lines back to include the separator
        start_line = max(0, page_line[start_pg] - 2)
    else:
        start_line = 0
    
    if end_pg in page_line:
        end_line = page_line[end_pg] - 2  # exclude next chapter's separator
    else:
        end_line = len(lines)
    
    chapter_text = "\n".join(lines[start_line:end_line])
    
    if ch_num == 0:
        fname = "00_frontmatter.txt"
    elif ch_num == 14:
        fname = "14_annexes.txt"
    else:
        fname = f"chapter{ch_num:02d}.txt"
    
    fpath = os.path.join(OUTDIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(chapter_text)
    
    num_pages = end_pg - start_pg
    num_lines = end_line - start_line
    print(f"{ch_num:3d}  {title:<45} P{start_pg:3d}-{end_pg-1:3d}  {num_lines:6d}  {len(chapter_text):7d}")

print(f"\n{'='*60}")
print("All chapter files written to:", OUTDIR)
