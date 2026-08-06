from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.health import router as health_router
from .api.upload import router as upload_router
from .api.chat import router as chat_router

app = FastAPI(
    title="DocMind AI",
    description="AI Powered PDF Chat Assistant",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to DocMind AI 🚀"
    }
