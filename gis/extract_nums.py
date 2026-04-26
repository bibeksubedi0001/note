import fitz

for pdf_name in ['COMPLETE Chapterwise Questions.pdf', 'ilovepdf_merged.pdf']:
    pdf_path = f'd:\\Final Year\\Theory\\gis\\{pdf_name}'
    doc = fitz.open(pdf_path)
    print(f'\n{"="*60}')
    print(f'{pdf_name} ({len(doc)} pages)')
    print("="*60)
    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text()
        for line in text.split('\n'):
            lo = line.lower().strip()
            if len(lo) < 3:
                continue
            if any(k in lo for k in ['rms','planimetric','distance between','rle','run-length','quadtree','block cod','idw','suitability','flow dir','flow acc','sink','watershed','river net','pour point','threshold','interpolat','calculate','compute','find the','lidar','1:2,','1:5,','1:20','1:25','1:30','encod','cell size','degree lat','degree lon']):
                print(f'  [p{i+1}] {line.strip()[:140]}')
    doc.close()
