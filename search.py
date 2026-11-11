
import json
import faiss

from sentence_transformers import SentenceTransformer

# 1. Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Load FAISS index
print("Loading FAISS index...")
index = faiss.read_index("vectorstore/financial.index")

# 3. Load chunk information
with open("vectorstore/chunks_metadata.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print("Search engine ready!")
print("Total searchable chunks:", len(chunks))


# 4. Create a search function
def search_report(question, top_k=3):

    # Convert question into an embedding
    question_vector = model.encode(
        [question],
        normalize_embeddings=True,
        convert_to_numpy=True
    )

    # Search FAISS for similar chunks
    scores, results = index.search(question_vector, top_k)

    print("\n========== SEARCH RESULTS ==========")
    print("Your question:", question)

    for rank, (score, result_index) in enumerate(
        zip(scores[0], results[0]), start=1
    ):
        if result_index == -1:
            continue

        chunk = chunks[int(result_index)]

        print(f"\n--- Result {rank} ---")
        print(f"Page number: {chunk['page']}")
        print(f"Similarity score: {score:.4f}")
        print("\nRelevant information:")
        print(chunk["text"][:1500])
        print("\n" + "=" * 50)


# 5. Ask questions continuously
while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower().strip() == "exit":
        print("Search engine closed.")
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    search_report(question)
