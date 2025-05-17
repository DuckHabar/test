import json
from pathlib import Path
from typing import List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class DocumentStore:
    """Load documents and perform simple TF-IDF retrieval."""

    def __init__(self, path: Path):
        self.documents = self._load_documents(path)
        self.vectorizer: TfidfVectorizer
        self.matrix
        self._build_index()

    def _load_documents(self, path: Path) -> List[dict]:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _build_index(self) -> None:
        texts = [d["text"] for d in self.documents]
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query: str) -> Tuple[int, str]:
        q_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(q_vec, self.matrix).flatten()
        best_idx = int(similarities.argmax())
        return self.documents[best_idx]["id"], self.documents[best_idx]["text"]
