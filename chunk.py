
import re
import json
from pathlib import Path

# 1. Load extracted text
input_path = Path("data/extracted_text.txt")

if not input_path.exists():
    print("ERROR: Extracted text file not found!")
    exit()

text = input_path.read_text(encoding="utf-8")

# 2. Separate the report into pages
pages = re.split(r"===== PAGE (\d+) =====", text)

page_data = []

for i in range(1, len(pages), 2):
    page_number = int(pages[i])
    page_text = pages[i + 1].strip()

    if page_text:
        page_data.append({
            "page": page_number,
            "text": page_text
        })

# 3. Set chunk size and overlap
CHUNK_SIZE = 700
OVERLAP = 100

chunks = []

# 4. Split each page into word-based chunks
for page in page_data:
    words = page["text"].split()

    start = 0

    while start < len(words):
        end = start + CHUNK_SIZE
        chunk_words = words[start:end]

        chunks.append({
            "chunk_id": len(chunks) + 1,
            "page": page["page"],
            "text": " ".join(chunk_words)
        })

        if end >= len(words):
            break

        start = end - OVERLAP

# 5. Save chunks as JSON
output_path = Path("data/chunks.json")
output_path.write_text(
    json.dumps(chunks, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

# 6. Display results
print("\n========== CHUNKING COMPLETE ==========")
print(f"Total pages processed: {len(page_data)}")
print(f"Total chunks created: {len(chunks)}")
print(f"Average words per chunk: {sum(len(c['text'].split()) for c in chunks) // max(len(chunks), 1)}")
print(f"Saved to: {output_path}")

print("\nFirst chunk preview:")
print(chunks[0]["text"][:500] if chunks else "No chunks created")
