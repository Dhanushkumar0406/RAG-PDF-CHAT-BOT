from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.services.pdf_service import PDFService
from app.services.embedding_service import EmbeddingService
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()

# Folder where uploaded PDFs will be stored
UPLOAD_FOLDER = Path("app/uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file, save it locally, and index it for the RAG pipeline.
    """

    if file.content_type != "application/pdf":
        return {
            "success": False,
            "message": "Only PDF files are allowed."
        }

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as pdf_file:
        pdf_file.write(await file.read())

    pipeline = RAGPipeline()
    pipeline.process_pdf(file_path)

    return {
        "success": True,
        "filename": file.filename,
        "message": "PDF uploaded and indexed successfully."
    }


@router.get("/read")
def read_pdf():
    pdf_path = UPLOAD_FOLDER / "sample.pdf"

    pdf_service = PDFService()
    text = pdf_service.extract_text(pdf_path)

    embedding_service = EmbeddingService()
    chunks = embedding_service.split_text(text)

    return {
        "total_characters": len(text),
        "total_chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else ""
    }
