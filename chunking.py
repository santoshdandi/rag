from parsing import load_pdf

def chunk_text(text, chunk_size, overlap):
    words = text.split(" ")
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(words), step):
        chunks.append(" ".join(words[i:i + chunk_size]))
        if (i + chunk_size) > len(words):
            break
    return chunks

def chunk_pages(pages, chunk_size=100, overlap=20):
    all_chunks = []
    for page in pages:
         for j, chunk in enumerate(chunk_text(page["text"], chunk_size, overlap)):
             all_chunks.append({
                "id": f"p{page['page']}-c{j}",
                "text": chunk,
                "page": page["page"],
                "source": page["source"],
            })
    return all_chunks

if __name__ == "__main__":
    pages = load_pdf("./Dandi_Nageswar_DevopsEngineer.pdf")
    chunks = chunk_pages(pages)
    print("Total chunks:", len(chunks))
    for c in chunks[:3]:
        print(f"\n--- {c['id']} (page {c['page']}) ---")
        print(c["text"])
