from services.vector_store import load_vector_store

def retrieve_documents(query, k=3):
    vector_store = load_vector_store()

    docs = vector_store.similarity_search(query, k=k)

    return [doc.page_content for doc in docs]