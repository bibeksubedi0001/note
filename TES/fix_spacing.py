import re
for fn in ['chapter5.html', 'chapter6.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'</span>\s+<span class="year-tag">', '</span><span class="year-tag">', c)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{fn}: spaces removed between year-tags')
