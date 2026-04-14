import fitz

# Extract chapter 1 content from both PDFs
for pdf_name in ['Manual.pdf', 'Bhatta & Kafle.pdf']:
    doc = fitz.open(pdf_name)
    print(f"\n{'='*80}")
    print(f"  {pdf_name}  —  {len(doc)} pages")
    print(f"{'='*80}")
    
    # Sample pages to find chapter 1 boundaries
    for i in range(min(40, len(doc))):
        text = doc[i].get_text()
        if any(kw in text.lower() for kw in ['chapter 1', 'technology', 'appropriate', 'definition', 'irreversible']):
            print(f"\n--- PAGE {i+1} ---")
            print(text[:1500])
    doc.close()
