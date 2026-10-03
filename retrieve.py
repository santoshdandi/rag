from embedding import embedding
from store import collection


def retrieve(query, top_k=3):
    query_vector = embedding([query])[0]
    results = collection.query(
        query_embeddings=[query_vector.tolist()],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        hits.append({
            "text": doc,
            "page": meta["page"],
            "source": meta["source"],
            "distance": dist,
            "similarity": 1 - dist / 2,
        })
    return hits
if __name__ == "__main__":
    questions = [
        "What CI/CD tools does he use?",
        "What security scanning tools does he know?",
        "How many years of experience does he have?",
        "What is his favorite food?",
    ]
    for q in questions:
        print(f"\n=== {q} ===")
        for h in retrieve(q):
            print(f"[page {h['page']} | similarity {h['similarity']:.3f}] {h['text'][:120]}...")