
from pypdf import PdfReader
from pathlib import Path

# 1. Locate the financial report
pdf_path = Path("data/financial_report.pdf")

# 2. Check whether the PDF exists
if not pdf_path.exists():
    print("ERROR: Financial PDF not found!")
    exit()

print("Opening financial report...")

# 3. Read the PDF
reader = PdfReader(str(pdf_path))

total_pages = len(reader.pages)

print(f"Total PDF pages: {total_pages}")

# 4. Extract text page by page
all_text = []
empty_pages = []

for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text() or ""

    if not text.strip():
        empty_pages.append(page_number)

    all_text.append(
        f"\n\n===== PAGE {page_number} =====\n\n{text}"
    )

    if page_number % 25 == 0:
        print(f"Processed {page_number}/{total_pages} pages")

# 5. Combine extracted text
final_text = "".join(all_text)

# 6. Save extracted text
output_path = Path("data/extracted_text.txt")

output_path.write_text(final_text, encoding="utf-8")

# 7. Display results
print("\n========== EXTRACTION COMPLETE ==========")

print(f"Total pages: {total_pages}")
print(f"Total characters: {len(final_text):,}")
print(f"Total words: {len(final_text.split()):,}")
print(f"Pages with no extractable text: {len(empty_pages)}")

if empty_pages:
    print(f"Empty pages: {empty_pages[:20]}")

print(f"\nExtracted text saved to: {output_path}")

