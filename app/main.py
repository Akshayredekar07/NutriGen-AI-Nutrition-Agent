from fastapi import FastAPI
from .routers import chat, ingest, history

app = FastAPI(title="RAG Nutrition Chatbot")

app.include_router(chat.router, prefix="/chat")
app.include_router(ingest.router, prefix="/ingest")
app.include_router(history.router, prefix="/history")
