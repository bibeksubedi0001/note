import fitz

for pdf_name in ['Manual.pdf', 'Bhatta & Kafle.pdf']:
    doc = fitz.open(pdf_name)
    print(f"\n{pdf_name} — {len(doc)} pages")
    for i in range(min(3, len(doc))):
        page = doc[i]
        text = page.get_text().strip()
        images = page.get_images()
        blocks = page.get_text("dict")["blocks"]
        n_text_blocks = sum(1 for b in blocks if b["type"] == 0)
        n_img_blocks = sum(1 for b in blocks if b["type"] == 1)
        print(f"  Page {i+1}: text_len={len(text)}, images={len(images)}, text_blocks={n_text_blocks}, img_blocks={n_img_blocks}")
        if text:
            print(f"    Text preview: {text[:200]}")
    doc.close()
