
import json
import numpy as np
import faiss

from pathlib import Path
from sentence_transformers import SentenceTransformer

# 1. Load our chunks
chunks_path = Path("data/chunks.json")

if not chunks_path.exists():
    print("ERROR: chunks.json not found!")
    exit()

with open(chunks_path, "r", encoding="utf-8") as file:
    chunks = json.load(file)

if not chunks:
    print("ERROR: No chunks found!")
    exit()

print(f"Loaded {len(chunks)} chunks.")

# 2. Load the embedding model
print("\nLoading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 3. Extract text from chunks
texts = [chunk["text"] for chunk in chunks]

# 4. Convert text into embeddings
print("\nCreating embeddings...")

embeddings = model.encode(
    texts,
    batch_size=16,
    show_progress_bar=True,
    normalize_embeddings=True,
    convert_to_numpy=True
)

embeddings = np.asarray(embeddings, dtype="float32")

# 5. Create FAISS vector index
print("\nBuilding FAISS index...")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

# 6. Save the index
Path("vectorstore").mkdir(exist_ok=True)

faiss.write_index(index, "vectorstore/financial.index")

# 7. Save chunk information
with open("vectorstore/chunks_metadata.json", "w", encoding="utf-8") as file:
    json.dump(chunks, file, ensure_ascii=False, indent=2)

# 8. Display results
print("\n========== EMBEDDINGS COMPLETE ==========")
print("Total chunks:", len(chunks))
print("Embedding dimensions:", dimension)
print("Vectors stored:", index.ntotal)
print("FAISS index saved successfully!")
