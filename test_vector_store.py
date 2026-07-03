from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vector_store import create_vector_store

docs = load_documents()
chunks = split_documents(docs)

create_vector_store(chunks)

print("✅ Vector Database Created Successfully!")