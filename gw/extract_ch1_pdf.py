import subprocess
import sys
import os

try:
    import fitz
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'PyMuPDF'], capture_output=True)
    import fitz

pdf_path = r'd:\Final Year\Theory\gw\chapter_wise\Groundwater Notes.pdf'
output_path = r'd:\Final Year\Theory\gw\chapter_wise\gw_ch1_extracted.txt'

if not os.path.exists(pdf_path):
    print(f"ERROR: File not found: {pdf_path}")
    sys.exit(1)

doc = fitz.open(pdf_path)
lines = []
lines.append(f"Total pages: {doc.page_count}")
for i, page in enumerate(doc):
    text = page.get_text()
    if text.strip():
        lines.append(f'--- PAGE {i+1} ---')
        lines.append(text)
doc.close()

result = '\n'.join(lines)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result)
print(f"Extracted {doc.page_count} pages to {output_path}")
print("DONE")
