from fastapi import APIRouter, HTTPException

from ..models.request_model import ChatRequest
from ..models.response_model import ChatResponse
from ..services.rag_pipeline import RAGPipeline

router = APIRouter()

pipeline = RAGPipeline()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(
    request: ChatRequest
):

    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Please enter a question.")

    try:
        answer = pipeline.ask(question)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=400, detail="Upload a PDF before asking a question.") from exc
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Unable to answer right now: {exc}") from exc

    return ChatResponse(
        answer=answer
    )
