import chromadb

client = chromadb.Client()
collection = client.create_collection("my_docs")

collection.add(
    documents=["Hello world", "Chroma is cool"],
    ids=["doc1", "doc2"]
)

results = collection.query(
    query_texts=["vector database"],
    n_results=2
)

print(results)
