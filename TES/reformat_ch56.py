"""
Phase 1: Bulk cleanup for TES chapters 5 and 6.
Removes:
  - Q-headings (<h3>Q1. ... </h3>)
  - Answer labels (<p><strong>Answer:</strong></p> and inline <strong>Answer:</strong>)
  - exam-ref spans from h2 headings
  - Cross-reference lines ("Refer to Q1 above", "Detailed answer same as Q1 above")
"""
import re

def clean_chapter(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    original = len(lines)
    out = []
    skip_next_blank = False

    for i, line in enumerate(lines):
        # 1) Remove Q-headings: <h3>Q1. ... </h3>
        if re.match(r'\s*<h3>Q\d+\.', line):
            skip_next_blank = True
            continue

        # 2) Remove standalone Answer lines
        stripped = line.strip()
        if stripped == '<p><strong>Answer:</strong></p>':
            skip_next_blank = True
            continue

        # 3) Remove lines that are cross-references
        if re.match(r'\s*<p>\(Refer to Q\d', stripped):
            skip_next_blank = True
            continue
        if re.match(r'\s*<p>\(Detailed answer same as Q\d', stripped):
            skip_next_blank = True
            continue
        # Single-line ref answers like "Key measures: Catalytic..." after a Refer line
        # -- keep these, they have actual summary content

        # 4) Remove exam-ref spans from h2 headings
        if '<h2>' in line and 'exam-ref' in line:
            line = re.sub(r'\s*<span class="exam-ref">[^<]*</span>', '', line)

        # Skip extra blank line after removed content
        if skip_next_blank and stripped == '':
            skip_next_blank = False
            continue
        skip_next_blank = False

        out.append(line)

    with open(fname, 'w', encoding='utf-8') as f:
        f.writelines(out)
    final = len(out)
    print(f"{fname}: {original} -> {final} lines (removed {original - final})")

if __name__ == '__main__':
    clean_chapter('chapter5.html')
    clean_chapter('chapter6.html')
    print("Phase 1 done!")
