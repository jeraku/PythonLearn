import chromadb
import uuid
from langchain_community.embeddings import OllamaEmbeddings


class ChromaMemory:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_store")

        self.collection = self.client.get_or_create_collection(
            name="agent_memory"
        )

        self.embedder = OllamaEmbeddings(
            model="nomic-embed-text"
        )

    def add(self, text: str):
        embedding = self.embedder.embed_query(text)

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(uuid.uuid4())]
        )

    def search(self, query: str, k=3):
        query_embedding = self.embedder.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        if results["documents"]:
            return results["documents"][0]

        return []