import fitz
import os

doc = fitz.open(r'd:\Final Year\Theory\gis\COMPLETE Chapterwise Questions.pdf')
out_dir = r'd:\Final Year\Theory\gis\pdf_pages'
os.makedirs(out_dir, exist_ok=True)

for i in range(len(doc)):
    page = doc[i]
    pix = page.get_pixmap(dpi=200)
    pix.save(os.path.join(out_dir, f'page_{i+1:02d}.png'))
    print(f'Saved page {i+1}')

doc.close()
print(f'Done - {len(doc)} pages saved to {out_dir}')
