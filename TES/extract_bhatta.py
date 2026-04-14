import fitz
import os

os.makedirs("d:/Final Year/Theory/TES/_tmp_pages", exist_ok=True)

doc = fitz.open("d:/Final Year/Theory/TES/Bhatta & Kafle.pdf")
for i in range(15):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    out = f"d:/Final Year/Theory/TES/_tmp_pages/bhatta_p{i+1:03d}.png"
    pix.save(out)
    print(f"Saved page {i+1}")
doc.close()
