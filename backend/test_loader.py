from app.vectorstore.loader import DocumentLoader

loader = DocumentLoader("../knowledge_base")

documents = loader.load_documents()

print("=" * 60)
print(f"Documents Loaded: {len(documents)}")

if documents:
    print()
    print("First Document:")
    print(documents[0]["metadata"])
    print()
    print(documents[0]["text"][:500])