from langchain_community.vectorstores import FAISS


class VectorStoreService:

    def create_vector_store(self, chunks, embedding_model):

        vector_store = FAISS.from_texts(
            texts=chunks,
            embedding=embedding_model
        )

        return vector_store

    def save_vector_store(self, vector_store, path):

        vector_store.save_local(path)

    def load_vector_store(self, path, embedding_model):

        return FAISS.load_local(
            path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

    def retrieve_documents(
        self,
        vector_store,
        question,
        k=4
    ):

        documents = vector_store.similarity_search(
            question,
            k=k
        )

        return documents