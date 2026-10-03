from sentence_transformers import SentenceTransformer, util
from parsing import load_pdf
from chunking import chunk_pages

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedding(text_resume):
    #print(type(chunks[0]["text"]))
    return model.encode(text_resume, normalize_embeddings=True)

if __name__=="__main__":
    pages = load_pdf("./Dandi_Nageswar_DevopsEngineer.pdf")
    chunks = chunk_pages(pages)
    texts = [c["text"] for c in chunks]
    #print(texts)
    vectors = embedding(texts)
    print(vectors)
    print("embedding shape", vectors.shape)