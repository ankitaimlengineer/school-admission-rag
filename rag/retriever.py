from langchain_chroma import Chroma
from rag.embeddings import get_embeddings

CHROMA_PATH = "chroma_db"

def get_retriever():

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever