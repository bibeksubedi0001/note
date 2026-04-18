import fitz
import os

os.chdir(r"D:\Final Year\Theory\cm")

files = [
    ('Ch1', 'Construction Mgmt Ch 1.pdf'),
    ('Ch2', 'Const Mgmt Ch 2.pdf'),
    ('Ch3', 'Const Mgmt (Ch- 3).pdf'),
    ('Ch4', 'Const Mgmt Ch 4.pdf'),
    ('Ch5', 'Const Mgmt Ch 5.pdf'),
    ('Ch6', 'Const Mgmt (Ch 6).pdf'),
]

with open('pdf_extract.txt', 'w', encoding='utf-8') as out:
    for label, path in files:
        doc = fitz.open(path)
        out.write(f'=== {label} ({len(doc)} pages) ===\n')
        for i, page in enumerate(doc):
            text = page.get_text().strip()
            if i < 4 or i == len(doc)-1:
                out.write(f'\n--- Page {i+1} ---\n')
                out.write(text[:2000] + '\n')
        doc.close()
        out.write('\n\n')
    print('Done')
