from rag.retriever import get_retriever

retriever = get_retriever()

query = "What is the admission process?"

docs = retriever.invoke(query)

print(f"\nRetrieved Documents: {len(docs)}\n")

for i, doc in enumerate(docs):
    print("=" * 50)
    print(f"Document {i+1}")
    print(doc.page_content[:500])