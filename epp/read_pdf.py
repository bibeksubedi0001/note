import fitz
import sys
doc = fitz.open(r'D:\Final Year\Theory\epp\Chapterwise Past Questions.pdf')
out = open(r'D:\Final Year\Theory\epp\pdf_output.txt', 'w', encoding='utf-8')
for i, page in enumerate(doc):
    text = page.get_text()
    out.write(f'=== PAGE {i+1} ===\n')
    out.write(text)
    out.write('\n\n')
doc.close()
out.close()
print('Done', file=sys.stderr)
