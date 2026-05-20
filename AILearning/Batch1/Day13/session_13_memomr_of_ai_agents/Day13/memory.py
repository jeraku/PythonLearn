import chromadb
import uuid
import redis
import json
from langchain_community.embeddings import OllamaEmbeddings


class MemoryManager:

    def __init__(self, session_id="default"):
        self.redis = redis.Redis(host="localhost", port=6379, decode_responses=True)
        self.session_id = session_id
        self.short_term_limit = 6  # Sliding window size

        self.client = chromadb.PersistentClient(path="./chroma_store")
        self.collection = self.client.get_or_create_collection("agent_memory")

        self.embedder = OllamaEmbeddings(model="nomic-embed-text")

    def add_short_term(self, role, content):
        key = f"chat:{self.session_id}"

        message = json.dumps({"role": role, "content": content})
        self.redis.rpush(key, message)

        # Sliding window trim
        self.redis.ltrim(key, -self.short_term_limit, -1)

    def get_short_term(self):
        key = f"chat:{self.session_id}"
        messages = self.redis.lrange(key, 0, -1)

        return [json.loads(m) for m in messages]


    def add_long_term(self, text):
        embedding = self.embedder.embed_query(text)

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(uuid.uuid4())]
        )

    def search_long_term(self, query, k=3):
        query_embedding = self.embedder.embed_query(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        return results

        # if results["documents"]:
        #     return results["documents"][0]

        # return []


    def should_store_long_term(self, text):
        # use llm to filter out good query: [Semantic, Preference, Summary]
        important_keywords = ["my name is", "i like", "i prefer", "remember"]
        return any(k in text.lower() for k in important_keywords)