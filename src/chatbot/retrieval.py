from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_index(docs: List[str]):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(docs)
    return vectorizer, matrix


def search(query: str, vectorizer: TfidfVectorizer, matrix):
    q_vec = vectorizer.transform([query])
    similarities = cosine_similarity(q_vec, matrix).flatten()
    return int(similarities.argmax())
