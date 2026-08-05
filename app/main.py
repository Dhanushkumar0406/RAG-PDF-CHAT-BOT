from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="DocMind AI",
    description="AI Powered PDF Chat Assistant",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to DocMind AI 🚀"
    }