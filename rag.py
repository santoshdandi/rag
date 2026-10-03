from retrieve import retrieve

LLM = "ollama"

SYSTEM_PROMPT = """You are a helpful assistant that answers questions about a document.
Answer ONLY using the provided context.
If the answer is not in the context, say: "I don't know based on the provided document."
Do not make up information. Mention the page number(s) you used."""

def build_prompt(question, hits):
    context = "\n\n".join(
        f"[Source: page {h['page']}]\n{h['text']}" for h in hits
    )
    return f"Context:\n{context}\n\nQuestion: {question}"

def generate(prompt):
    if LLM == "ollama":
        import ollama
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            options={"temperature": 0},
        )
        return response["message"]["content"]

def ask(question, top_k=3, show_context=False):
    hits = retrieve(question, top_k=top_k)
    prompt = build_prompt(question, hits)
    if show_context:
        print("----- PROMPT SENT TO LLM -----")
        print(prompt)
        print("------------------------------")
    return generate(prompt)

if __name__ == "__main__":
    questions = [
        "What CI/CD tools does he use?",
        "What security scanning tools does he know?",
        "How many years of experience does he have?",
        "What are the organizations he worked for?"
    ]
    for q in questions:
        print(f"\nQ: {q}")
        print("A:", ask(q))