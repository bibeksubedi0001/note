import re

def reformat_chapter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 1. Remove <span class="exam-ref">...</span> from h2 lines
        if '<h2>' in line and 'exam-ref' in line:
            line = re.sub(r'\s*<span class="exam-ref">.*?</span>', '', line)
        
        # 2. Remove <h3>Q#. ... </h3> lines entirely
        if re.search(r'<h3>Q\d+\.', line):
            i += 1
            continue
        
        # 3. Remove <p><strong>Answer:</strong></p> lines
        if '<p><strong>Answer:</strong></p>' in line.strip():
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print(f"Processed {filepath}: {len(lines)} -> {len(new_lines)} lines")

reformat_chapter('chapter1_updated.html')
reformat_chapter('chapter2.html')
