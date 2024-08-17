from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# This is a simplified RAG system. In a real-world scenario, you'd have a more sophisticated setup.
model = SentenceTransformer('all-MiniLM-L6-v2')

# Pretend this is our knowledge base
knowledge_base = [
    "The capital of France is Paris.",
    "Python is a programming language.",
    "Machine learning is a subset of artificial intelligence.",
    "The Earth orbits around the Sun.",
]

knowledge_embeddings = model.encode(knowledge_base)

def get_rag_response(query):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, knowledge_embeddings)[0]
    most_similar_idx = np.argmax(similarities)
    return knowledge_base[most_similar_idx]