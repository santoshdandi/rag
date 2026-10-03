from operator import index

import chromadb

import embedding
from parsing import load_pdf
from chunking import chunk_pages
from embedding import embedding

client = chromadb.PersistentClient(path= "chroma_db")
collection = client.get_or_create_collection(name="resume")

def index_document(path):
    pages = load_pdf(path)
    chunks = chunk_pages(pages)
    texts = [c["text"] for c in chunks]
    vectors = embedding(texts)
    collection.upsert(
        ids=[c["id"] for c in chunks],
        documents=texts,
        embeddings=vectors.tolist(),
        metadatas=[{"page": c["page"], "source": c["source"]} for c in chunks],
    )
    return len(chunks)

if __name__ == "__main__":
    n = index_document("./Dandi_Nageswar_DevopsEngineer.pdf")
    print("indexed chunks", n)
    print("Total in collection", collection.count())
    print(collection.get(ids=["p1-c0"]))