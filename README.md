# User Support Chatbot

This project provides a minimal prototype of a user support chatbot that can be run entirely locally.  The chatbot indexes a small collection of documents with TF‑IDF and serves answers through a FastAPI application.  A very simple HTML front end is included.

The project purposely avoids any external language model APIs to prevent data leakage.  All processing happens locally using scikit‑learn and Python.

## Project Structure

- `data/documents.json` – example knowledge base documents.
- `src/app.py` – FastAPI server serving the chat API and static front end.
- `src/chatbot/document_store.py` – loads documents and performs TF‑IDF search.
- `src/chatbot/generator.py` – placeholder generator returning the retrieved document.
- `src/static/index.html` – minimal chat interface.
- `tests/` – unit test for the document search logic.

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the API server:

```bash
python -m src.app
```

3. Open your browser at `http://localhost:8000` and try asking a question.  Alternatively you can send a request with `curl`:

```bash
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' -d '{"question": "Как сбросить пароль?"}'
```

## Notes

This repository is a small demonstration of the project idea and is not a full production system.  It can serve as a starting point for further development, evaluation and deployment inside a secure environment.
