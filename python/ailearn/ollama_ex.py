# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)
# sentences = ['search_query: Who is Laurens van Der Maaten?']
# embeddings = model.encode(sentences)
# print(embeddings)

import ollama
import chromadb

def ollama_embed(text):
    embeddings=[]
    for t in text:
        res = ollama.embeddings(model='nomic-embed-text', prompt=t)
        embeddings.append(res["embedding"])
    return embeddings


docs= [
    "this is good programming language",
    "create a fastapi for builing API",
    "I love python and machine learning"
]

# client = chromadb.Client()
# collection = client.create_collection("ollama demo")
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="personal_collection")
emb = ollama_embed(docs)


collection.add(
    documents = docs,
    embeddings = emb,
    ids=[str(i) for i in range(len(docs))]
)

print("ollama adding ocmpleted")

query= "tell me about vectordb"
# q_emb= ollama_embed(query)
q_emb = ollama_embed([query])




result = collection.query(query_embeddings=q_emb, n_results=2,include=["documents", "distances", "embeddings"] )
print( result)