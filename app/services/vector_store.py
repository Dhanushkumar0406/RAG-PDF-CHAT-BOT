from langchain_community.vectorstores import FAISS


class VectorStoreService:

    def create_vector_store(
        self,
        chunks,
        embedding_model
    ):

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embedding_model
        )

        return vector_store

    def save_vector_store(
        self,
        vector_store,
        save_path
    ):

        vector_store.save_local(save_path)

    def load_vector_store(
        self,
        save_path,
        embedding_model
    ):

        vector_store = FAISS.load_local(
            save_path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

        return vector_store