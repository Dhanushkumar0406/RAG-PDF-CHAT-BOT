from app.services.embedding_service import EmbeddingService
from app.services.vector_store import VectorStoreService

embedding = EmbeddingService()

vector = VectorStoreService()

db = vector.load_vector_store(
    "app/vector_db",
    embedding.get_embedding_model()
)

docs = vector.retrieve_documents(
    db,
    "What is Artificial Intelligence?"
)

print("\nRetrieved Documents\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 50)
    print(f"Chunk {i}")
    print(doc.page_content)