from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .chatbot.document_store import DocumentStore
from .chatbot import generator

app = FastAPI()

# Load documents from JSON at startup
store = DocumentStore(Path(__file__).resolve().parent.parent / "data" / "documents.json")

app.mount("/static", StaticFiles(directory=Path(__file__).resolve().parent / "static"), name="static")


class Question(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def index():
    with open(Path(__file__).resolve().parent / "static" / "index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat")
def chat(q: Question):
    _id, doc_text = store.search(q.question)
    answer = generator.generate_answer(q.question, doc_text)
    return {"answer": answer}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
