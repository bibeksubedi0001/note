"""
Bulk reformat TES chapter3.html and chapter4.html:
1. Remove <span class="exam-ref">...</span> from <h2> lines
2. Remove <h3>Q\d+. ... headings
3. Remove <p><strong>Answer:</strong></p> lines
4. Clean up multiple blank lines
"""
import re, sys

def reformat(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_count = len(lines)
    result = []
    skip_next_answer = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # 1. Remove exam-ref spans from h2 lines
        if '<h2>' in line and 'exam-ref' in line:
            line = re.sub(r'\s*<span class="exam-ref">.*?</span>', '', line)

        # 2. Remove Q-heading lines: <h3>Q1. ... or <h3>Q2. ...
        if re.match(r'\s*<h3>Q\d+\.', stripped):
            skip_next_answer = True
            continue

        # 3. Remove Answer lines right after Q-headings
        if skip_next_answer:
            skip_next_answer = False
            if '<strong>Answer:</strong>' in stripped:
                continue

        result.append(line)

    # 4. Clean multiple blank lines (3+ newlines → 2)
    content = ''.join(result)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    new_count = content.count('\n') + 1
    print(f"{filename}: {original_count} -> {new_count} lines (removed {original_count - new_count})")

reformat('chapter3.html')
reformat('chapter4.html')
print("Done!")
