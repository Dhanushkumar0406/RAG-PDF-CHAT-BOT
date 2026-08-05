from langchain.text_splitter import RecursiveCharacterTextSplitter


class EmbeddingService:
    """
    Responsible for preparing text for embeddings.
    """

    def split_text(self, text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100,
            length_function=len
        )

        chunks = splitter.split_text(text)

        return chunks
