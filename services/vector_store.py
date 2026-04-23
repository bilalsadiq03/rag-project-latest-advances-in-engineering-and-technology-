from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    return vector_store


def save_vector_store(vector_store, path="faiss_index"):
    vector_store.save_local(path)


def load_vector_store(path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    return FAISS.load_local(path, embeddings)