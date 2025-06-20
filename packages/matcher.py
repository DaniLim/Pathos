"""Prototype module for cross-language matching using offline embeddings."""

import numpy as np


def most_similar(embedding, embedding_matrix, words, top_k=5):
    """Return the top_k most similar words based on cosine similarity."""
    norms = np.linalg.norm(embedding_matrix, axis=1)
    sims = np.dot(embedding_matrix, embedding) / (norms * np.linalg.norm(embedding) + 1e-9)
    best_idx = np.argsort(-sims)[:top_k]
    return [(words[i], float(sims[i])) for i in best_idx]
