from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def encode_texts(texts):
    return MODEL.encode(texts, convert_to_numpy=True)
