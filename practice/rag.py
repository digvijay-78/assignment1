# import numpy as np

# document = """
# Python is a popular programming language.

# Pandas is commonly used for data analysis.

# NumPy provides tools for numerical computing.

# FastAPI is a Python framework for building APIs.
# """

# chunks = [
#     "Python is a popular programming language.",
#     "Pandas is commonly used for data analysis.",
#     "NumPy provides tools for numerical computing.",
#     "FastAPI is a Python framework for building APIs."
# ]

# response = client.embeddings.create(
#     model="YOUR_EMBEDDING_MODEL",
#     input=chunks
# )

# vectors = [item.embedding for item in response.data]
# faiss.normalize_L2(vectors)
# index = faiss.IndexFlatIP(dimension)
# index.add(vectors)

# question = "What can I use for data analysis?"
# response = client.embeddings.create(
#     model="YOUR_EMBEDDING_MODEL",
#     input=question
# )

# query_vector = response.data[0].embedding
# faiss.normalize_L2(query_vector)
# scores, indices = index.search(query_vector, k=2)

import os
import numpy as np
import faiss
import fitz
from dotenv import load_dotenv
from openai import OpenAI


# -----------------------------
# 1. Setup
# -----------------------------

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PDF_PATH = "document.pdf"

EMBEDDING_MODEL = "YOUR_EMBEDDING_MODEL"
LLM_MODEL = "YOUR_LLM_MODEL"


# -----------------------------
# 2. Extract PDF text
# -----------------------------

def load_pdf(path):
    documents = []

    doc = fitz.open(path)

    for page_number, page in enumerate(doc):
        text = page.get_text().strip()

        if text:
            documents.append({
                "text": text,
                "page": page_number + 1
            })

    return documents


# -----------------------------
# 3. Chunk text
# -----------------------------

def create_chunks(documents, chunk_size=1000, overlap=100):

    chunks = []

    for document in documents:

        text = document["text"]
        page = document["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "page": page
            })

            start += chunk_size - overlap

    return chunks


# -----------------------------
# 4. Create embeddings
# -----------------------------

def create_embeddings(texts):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    vectors = [
        item.embedding
        for item in response.data
    ]

    return np.asarray(vectors, dtype="float32")


# -----------------------------
# 5. Create FAISS index
# -----------------------------

def create_index(vectors):

    faiss.normalize_L2(vectors)

    dimension = vectors.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(vectors)

    return index


# -----------------------------
# 6. Search
# -----------------------------

def search(question, index, chunks, k=3):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=question
    )

    query_vector = np.asarray(
        [response.data[0].embedding],
        dtype="float32"
    )

    faiss.normalize_L2(query_vector)

    scores, indices = index.search(
        query_vector,
        k
    )

    results = []

    for score, index_number in zip(
        scores[0],
        indices[0]
    ):

        results.append({
            "text": chunks[index_number]["text"],
            "page": chunks[index_number]["page"],
            "score": float(score)
        })

    return results


# -----------------------------
# 7. Generate answer
# -----------------------------

def generate_answer(question, results):

    context = "\n\n".join(
        f"[Page {result['page']}]\n{result['text']}"
        for result in results
    )

    prompt = f"""
Answer the user's question using ONLY the provided context.

If the answer is not present in the context,
say that the information is not available in the document.

Context:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model=LLM_MODEL,
        input=prompt
    )

    return response.output_text


# -----------------------------
# 8. Main RAG pipeline
# -----------------------------

def main():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Pages loaded: {len(documents)}")


    print("Creating chunks...")

    chunks = create_chunks(documents)

    print(f"Chunks created: {len(chunks)}")


    print("Creating embeddings...")

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    vectors = create_embeddings(texts)

    print("Embeddings created.")


    print("Building FAISS index...")

    index = create_index(vectors)

    print("RAG system ready!")

    print("\nAsk questions about your PDF.")
    print("Type 'exit' to stop.\n")


    while True:

        question = input("You: ")

        if question.lower() == "exit":
            break

        results = search(
            question,
            index,
            chunks,
            k=3
        )

        print("\nRetrieved chunks:")

        for result in results:
            print(
                f"Page {result['page']} "
                f"| Score: {result['score']:.3f}"
            )

        answer = generate_answer(
            question,
            results
        )

        print("\nBot:")
        print(answer)

        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
