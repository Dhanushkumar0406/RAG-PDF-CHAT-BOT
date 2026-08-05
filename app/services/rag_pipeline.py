from pathlib import Path

from app.services.pdf_service import PDFService
from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStoreService


class RAGPipeline:

    def __init__(self):

        self.pdf_service = PDFService()

        self.embedding_service = EmbeddingService()

        self.vector_service = VectorStoreService()

    def process_pdf(
        self,
        pdf_path: Path
    ):

        print("\nReading PDF...")

        text = self.pdf_service.extract_text(pdf_path)

        print("PDF Read Successfully")

        print("\nSplitting Text...")

        chunks = self.embedding_service.split_text(text)

        print(f"Total Chunks : {len(chunks)}")

        print("\nLoading Embedding Model...")

        embedding_model = self.embedding_service.get_embedding_model()

        print("Embedding Model Ready")

        print("\nCreating FAISS...")

        vector_store = self.vector_service.create_vector_store(
            chunks,
            embedding_model
        )

        print("FAISS Created")

        print("\nSaving FAISS...")

        self.vector_service.save_vector_store(
            vector_store,
            "app/vector_db"
        )

        print("FAISS Saved Successfully")