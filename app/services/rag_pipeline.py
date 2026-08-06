from pathlib import Path

from .embedding_service import EmbeddingService
from .vector_store import VectorStoreService
from .llm_service import LLMService
from .pdf_service import PDFService


VECTOR_DB_FOLDER = Path(__file__).resolve().parents[1] / "vector_db"


class RAGPipeline:

    def __init__(self):

        self.vector = VectorStoreService()
        self.llm = LLMService()
        self.pdf = PDFService()
        self.embedding = None

    def _embedding_service(self):
        """Load the embedding model only when a PDF is indexed or queried."""
        if self.embedding is None:
            self.embedding = EmbeddingService()
        return self.embedding

    def process_pdf(self, file_path):
        text = self.pdf.extract_text(file_path)
        chunks = self._embedding_service().split_text(text)

        if not chunks:
            raise ValueError("No readable text was found in this PDF.")

        embedding_model = self._embedding_service().get_embedding_model()
        db = self.vector.create_vector_store(chunks, embedding_model)
        self.vector.save_vector_store(db, str(VECTOR_DB_FOLDER))
        return len(chunks)

    def ask(self, question):

        embedding_model = self._embedding_service().get_embedding_model()
        db = self.vector.load_vector_store(
            str(VECTOR_DB_FOLDER),
            embedding_model
        )

        docs = self.vector.retrieve_documents(
            db,
            question
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        answer = self.llm.generate_answer(
            context,
            question
        )

        return answer
