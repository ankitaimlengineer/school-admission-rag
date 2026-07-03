from rag.loader import load_documents

docs = load_documents()

print("Total Documents :", len(docs))

for doc in docs:
    print(doc.metadata["source"])