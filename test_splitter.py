from rag.loader import load_documents
from rag.splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print("=" * 50)
print("Total Documents :", len(documents))
print("Total Chunks :", len(chunks))
print("=" * 50)

for i, chunk in enumerate(chunks[:5]):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk.page_content[:300])