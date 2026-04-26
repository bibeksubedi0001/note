import fitz
doc = fitz.open(r'd:\Final Year\Theory\gis\COMPLETE Chapterwise Questions.pdf')
text = '\n'.join([page.get_text() for page in doc])
with open(r'd:\Final Year\Theory\gis\extracted_q.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Done: {len(doc)} pages, {len(text)} chars')
doc.close()
