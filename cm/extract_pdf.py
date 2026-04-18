import fitz
import os

pdf_path = r"D:\Final Year\Theory\cm\Santosh Kumar Shrestha.pdf"
out_dir = r"D:\Final Year\Theory\cm\ocr_output"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

# Check if pages have text or are scanned
has_text = 0
no_text = 0
for i in range(min(10, len(doc))):
    t = doc[i].get_text().strip()
    if len(t) > 20:
        has_text += 1
    else:
        no_text += 1
    print(f"Page {i+1}: {len(t)} chars -> {'TEXT' if len(t)>20 else 'IMAGE/EMPTY'}")

print(f"\nFirst 10 pages: {has_text} with text, {no_text} without")

# Extract text from first 3 pages to see content
for i in range(min(3, len(doc))):
    t = doc[i].get_text()
    print(f"\n{'='*60}")
    print(f"PAGE {i+1}")
    print('='*60)
    print(t[:500] if t.strip() else "[NO TEXT]")

doc.close()
