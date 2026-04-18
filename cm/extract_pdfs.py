import fitz

# Extract past questions
doc = fitz.open('Chapterwise Past Questions.pdf')
with open('past_questions_text.txt', 'w', encoding='utf-8') as f:
    for i in range(doc.page_count):
        text = doc[i].get_text()
        if text.strip():
            f.write(f'--- Page {i+1} ---\n')
            f.write(text)
            f.write('\n')
doc.close()
print('Done extracting past questions')

# Extract reference pages from book
doc = fitz.open('Santosh Kumar Shrestha.pdf')
with open('reference_pages.txt', 'w', encoding='utf-8') as f:
    page_ranges = [(39, 46), (51, 66), (206, 214), (327, 333)]
    for start, end in page_ranges:
        for i in range(start, end):
            if i < doc.page_count:
                text = doc[i].get_text()
                if text.strip():
                    f.write(f'=== PDF Page {i+1} ===\n')
                    f.write(text)
                    f.write('\n')
doc.close()
print('Done extracting reference pages')
