from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


class EmbeddingService:

    def __init__(self):

        try:
            self.embedding_model = HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-en-v1.5"
            )
        except Exception as exc:
            raise RuntimeError(
                "The embedding model could not be loaded. Check your internet connection "
                "and SSL certificates, then retry the upload."
            ) from exc

    def split_text(self, text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )

        return splitter.split_text(text)

    def get_embedding_model(self):

        return self.embedding_model
