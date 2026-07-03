from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

CHROMA_PATH = "chroma_db"


def create_vector_store(chunks):

    embeddings = get_embeddings()

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    return vector_db