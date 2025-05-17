import unittest
from pathlib import Path

try:
    from src.chatbot.document_store import DocumentStore
    SKLEARN_AVAILABLE = True
except ModuleNotFoundError:
    SKLEARN_AVAILABLE = False


class RetrievalTest(unittest.TestCase):
    @unittest.skipUnless(SKLEARN_AVAILABLE, "scikit-learn is not installed")
    def test_search_returns_expected_document(self):
        store = DocumentStore(Path(__file__).resolve().parent.parent / 'data' / 'documents.json')
        _id, text = store.search('как сбросить пароль?')
        self.assertEqual(_id, 1)
        self.assertIn('сбросить пароль', text.lower())


if __name__ == '__main__':
    unittest.main()
