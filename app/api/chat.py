from fastapi import APIRouter

from app.models.request_model import ChatRequest
from app.models.response_model import ChatResponse
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()

pipeline = RAGPipeline()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(
    request: ChatRequest
):

    answer = pipeline.ask(
        request.question
    )

    return ChatResponse(
        answer=answer
    )