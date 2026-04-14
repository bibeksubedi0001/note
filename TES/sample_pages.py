import fitz

for pdf_name in ['Manual.pdf', 'Bhatta & Kafle.pdf']:
    doc = fitz.open(pdf_name)
    print(f"\n{'='*80}")
    print(f"  {pdf_name}  —  {len(doc)} pages")
    print(f"{'='*80}")
    for i in range(min(10, len(doc))):
        text = doc[i].get_text()
        print(f"\n--- PAGE {i+1} ---")
        print(text[:600])
    doc.close()
