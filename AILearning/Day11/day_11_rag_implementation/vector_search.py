import requests
import pandas as pd
import uuid

import chromadb
from chromadb.config import Settings


client = chromadb.PersistentClient(path="./chroma_imdb")

collection = client.get_or_create_collection(
    name="movies"
)

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"
df = pd.read_csv("imdb_processed.csv")


def get_embedding(text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": text
        }
    )

    response.raise_for_status()
    return response.json()["embedding"]


if collection.count() == 0:
    embeddings = []
    documents = []
    metadatas = []
    ids = []

    for _, row in df.iterrows():
        desc = str(row["Description"])
        
        embedding = get_embedding(desc)
        
        embeddings.append(embedding)
        documents.append(desc)
        metadatas.append(row.to_dict())
        ids.append(str(uuid.uuid4()))

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
    )


def search_movies(query, n_results=11):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results

query = input("Enter Genre ")
results = search_movies(query)

for movie in results["metadatas"][0]:
    print("=" * 30)
    print(movie.get("Movie Name"))
