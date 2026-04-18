"""
Full OCR extraction of Santosh Kumar Shrestha CM PDF
Uses PyMuPDF to render pages -> pytesseract for OCR
Outputs chapter-wise text files
Supports resume: skips pages already in checkpoint file
"""
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io, os, re, sys, time, json

# Config
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
PDF_PATH = r"D:\Final Year\Theory\cm\Santosh Kumar Shrestha.pdf"
OUT_DIR  = r"D:\Final Year\Theory\cm\ocr_output"
CHECKPOINT = os.path.join(OUT_DIR, "_checkpoint.json")
DPI = 250

os.makedirs(OUT_DIR, exist_ok=True)

# Load checkpoint if exists (for resume)
done_pages = {}
if os.path.exists(CHECKPOINT):
    with open(CHECKPOINT, 'r', encoding='utf-8') as f:
        done_pages = json.load(f)
    print(f"Resuming: {len(done_pages)} pages already done")

doc = fitz.open(PDF_PATH)
total = len(doc)
print(f"PDF: {total} pages | DPI: {DPI}")
print("=" * 60)
sys.stdout.flush()

all_text = [""] * total  # pre-fill
# Load already-done pages
for k, v in done_pages.items():
    idx = int(k)
    if idx < total:
        all_text[idx] = v

start = time.time()
newly_done = 0

for i in range(total):
    if str(i) in done_pages:
        continue  # skip already-OCR'd pages

    try:
        page = doc[i]
        mat = fitz.Matrix(DPI/72, DPI/72)
        pix = page.get_pixmap(matrix=mat)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img, lang='eng')
    except Exception as e:
        text = f"[OCR ERROR on page {i+1}: {e}]"
        print(f"  ERROR page {i+1}: {e}")

    block = f"\n\n{'='*60}\nPAGE {i+1}\n{'='*60}\n{text}"
    all_text[i] = block
    done_pages[str(i)] = block
    newly_done += 1

    # Save checkpoint every 10 pages
    if newly_done % 10 == 0:
        with open(CHECKPOINT, 'w', encoding='utf-8') as f:
            json.dump(done_pages, f)

    # Progress
    total_done = len(done_pages)
    elapsed = time.time() - start
    rate = newly_done / elapsed if elapsed > 0 else 0
    remaining = total - total_done
    eta = remaining / rate if rate > 0 else 0
    if newly_done % 5 == 0 or newly_done == 1:
        print(f"  Page {i+1:>3}/{total} | done={total_done} | {elapsed:.0f}s | ~{eta:.0f}s left | {rate:.1f} pg/s")
        sys.stdout.flush()

doc.close()

# Final checkpoint save
with open(CHECKPOINT, 'w', encoding='utf-8') as f:
    json.dump(done_pages, f)

# Save full text
full_path = os.path.join(OUT_DIR, "full_ocr_text.txt")
with open(full_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_text))
print(f"\nFull text saved: {full_path}")
print(f"Total time: {time.time()-start:.0f}s ({newly_done} new pages)")

# --- Chapter detection & splitting ---
# Patterns for chapter headings in this textbook:
# "1. CONSTRUCTION MANAGEMENT FRAMEWORK" or "CHAPTER 1" etc.
chapter_patterns = [
    re.compile(r'(?:^|\n)\s*(\d{1,2})\.\s+[A-Z][A-Z\s,&/\-]{5,}', re.MULTILINE),
    re.compile(r'(?:^|\n)\s*(?:CHAPTER|Chapter)\s*[\-:\s]*(\d{1,2})\b', re.IGNORECASE),
]

splits = []
current_chapter = "00_frontmatter"
current_text = []

for block in all_text:
    if not block:
        continue
    found_ch = None
    for pat in chapter_patterns:
        m = pat.search(block)
        if m:
            ch_num = int(m.group(1))
            if 1 <= ch_num <= 20:  # valid chapter range
                found_ch = ch_num
                break

    if found_ch is not None and f"chapter{found_ch:02d}" != current_chapter:
        # Save previous
        if current_text:
            splits.append((current_chapter, '\n'.join(current_text)))
        current_chapter = f"chapter{found_ch:02d}"
        current_text = [block]
    else:
        current_text.append(block)

if current_text:
    splits.append((current_chapter, '\n'.join(current_text)))

# Write chapter files
print(f"\nDetected {len(splits)} sections:")
for name, text in splits:
    ch_path = os.path.join(OUT_DIR, f"{name}.txt")
    with open(ch_path, 'w', encoding='utf-8') as f:
        f.write(text)
    lines = text.count('\n')
    print(f"  {name}.txt ({lines} lines, {len(text)} chars)")

print("\nAll done!")
