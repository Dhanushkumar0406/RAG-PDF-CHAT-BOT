from app.services.embedding_service import EmbeddingService

embedding = EmbeddingService()

print("Loading Model...")

model = embedding.get_embedding_model()

print("Model Loaded Successfully!")