import fitz
import os

os.makedirs('pdf_images', exist_ok=True)

# Extract pages with numerical problems as images
doc = fitz.open('Chapterwise Past Questions.pdf')
pages_to_extract = [3, 4, 5, 6, 7, 8, 9, 10, 16, 20, 21, 32, 33, 34, 35, 36]  # 0-indexed

for pg in pages_to_extract:
    if pg < doc.page_count:
        page = doc[pg]
        mat = fitz.Matrix(2, 2)  # 2x zoom for readability
        pix = page.get_pixmap(matrix=mat)
        pix.save(f'pdf_images/page_{pg+1}.png')
        print(f'Saved page {pg+1}')

doc.close()
print('Done!')
