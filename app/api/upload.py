from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from ..services.pdf_service import PDFService
from ..services.embedding_service import EmbeddingService
from ..services.rag_pipeline import RAGPipeline

router = APIRouter()

# Folder where uploaded PDFs will be stored
APP_FOLDER = Path(__file__).resolve().parents[1]
UPLOAD_FOLDER = APP_FOLDER / "uploads"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file, save it locally, and index it for the RAG pipeline.
    """

    if file.content_type != "application/pdf" and not (file.filename or "").lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    filename = Path(file.filename or "document.pdf").name
    file_path = UPLOAD_FOLDER / filename

    with open(file_path, "wb") as pdf_file:
        pdf_file.write(await file.read())

    try:
        pipeline = RAGPipeline()
        chunk_count = pipeline.process_pdf(file_path)
    except Exception as exc:
        file_path.unlink(missing_ok=True)
        raise HTTPException(status_code=400, detail=f"Unable to index this PDF: {exc}") from exc

    return {
        "success": True,
        "filename": filename,
        "chunks": chunk_count,
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
