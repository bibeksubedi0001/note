import fitz
import os

os.makedirs("d:/Final Year/Theory/TES/_tmp_pages", exist_ok=True)

for pdf_name, prefix in [('Manual.pdf', 'manual'), ('Bhatta & Kafle.pdf', 'bhatta')]:
    doc = fitz.open(pdf_name)
    # Extract first 30 pages as images to find chapter 1
    for i in range(min(30, len(doc))):
        page = doc[i]
        pix = page.get_pixmap(dpi=200)
        out = f"d:/Final Year/Theory/TES/_tmp_pages/{prefix}_p{i+1:03d}.png"
        pix.save(out)
    print(f"{pdf_name}: extracted {min(30, len(doc))} pages")
    doc.close()
