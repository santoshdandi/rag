from pypdf import PdfReader

def load_pdf(path):
    """ Load pdf file """
    reader = PdfReader(path)
    #print(reader.pages)
    #print(enumerate(reader.pages))
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        #print(text)
        pages.append({"text": text, "page": i + 1, "source": path})
    #print(pages)
    #print(len(pages))
    return pages
if __name__ == "__main__":
    pages = load_pdf("./Dandi_Nageswar_DevopsEngineer.pdf")
    print("Total pages:", len(pages))
    print(pages[0]["text"][:500])