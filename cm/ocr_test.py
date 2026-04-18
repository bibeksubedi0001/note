"""Quick test: OCR first 5 pages to check quality"""
import fitz, pytesseract, io, time
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
doc = fitz.open(r"D:\Final Year\Theory\cm\Santosh Kumar Shrestha.pdf")

start = time.time()
for i in range(5):
    page = doc[i]
    mat = fitz.Matrix(250/72, 250/72)
    pix = page.get_pixmap(matrix=mat)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    text = pytesseract.image_to_string(img, lang='eng')
    print(f"\n--- PAGE {i+1} ({time.time()-start:.1f}s) ---")
    print(text[:600])

doc.close()
print(f"\nTotal: {time.time()-start:.1f}s for 5 pages")
print(f"Estimated full (386 pages): {(time.time()-start)/5*386:.0f}s = {(time.time()-start)/5*386/60:.0f} min")
