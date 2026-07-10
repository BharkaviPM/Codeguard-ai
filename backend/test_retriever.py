from app.vectorstore.retriever import Retriever

retriever = Retriever()

results = retriever.search(

    "What is SQL Injection?",

    top_k=3

)

print("=" * 80)

print(f"Results Found : {len(results)}")

print("=" * 80)

for result in results:

    print()

    print(result["metadata"])

    print()

    print(result["text"][:400])

    print()

    print("-" * 80)