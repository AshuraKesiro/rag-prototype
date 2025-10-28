from fastapi import FastAPI
from app.embeddings import encode_texts
import faiss
import numpy as np

app = FastAPI(title="RAG Prototype")

docs = [
    "FastAPI is a modern, fast web framework for building APIs with Python.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors.",
    "Sentence-transformers provide easy-to-use embeddings for semantic search."
]

vectors = encode_texts(docs)
dim = vectors.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(vectors)

@app.get("/search")
async def search(q: str, k: int = 2):
    qv = encode_texts([q])
    D, I = index.search(qv, k)
    results = [{"id": int(i), "doc": docs[int(i)], "dist": float(D[0][idx])} for idx,i in enumerate(I[0])]
    return {"results": results}
