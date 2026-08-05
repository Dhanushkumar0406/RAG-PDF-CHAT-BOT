from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStoreService
from app.services.llm_service import LLMService


class RAGPipeline:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.vector = VectorStoreService()

        self.llm = LLMService()

    def ask(self, question):

        db = self.vector.load_vector_store(
            "app/vector_db",
            self.embedding.get_embedding_model()
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