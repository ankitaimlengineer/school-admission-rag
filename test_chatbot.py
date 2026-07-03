from chatbot import ask_question

question = input("Ask Question: ")

answer, docs = ask_question(question)

print("\nAnswer:\n")
print(answer)

print("\nSources Used:")
sources = set()

for doc in docs:
    source = doc.metadata.get("source")
    if source:
        sources.add(source)

print("\nSources Used:")
for source in sources:
    print(source)