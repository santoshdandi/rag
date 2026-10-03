from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-V2')

sentences = [
    "Kubernetes security",
    "Securing container clusters",
    "Cooking pasta at home",
]

vectors = model.encode(sentences)

print("vector share::", vectors.shape)
print("first 5 number of 1st vector", vectors[0][:5])

print("\nSimilarity 1 vs 2:", util.cos_sim(vectors[0], vectors[1]).item())
print("Similarity 1 vs 3:", util.cos_sim(vectors[0], vectors[2]).item())