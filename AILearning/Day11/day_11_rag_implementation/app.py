from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda

from groq_client import call_groq
import os


PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "pdf_collection"


# 1. LOAD PDF
def load_pdf(path):
    loader = PyPDFLoader(path)
    return loader.load()


def clean_text(text: str) -> str:
    return text.encode("utf-8", "ignore").decode("utf-8")


# 2. SPLIT
def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    # cleaning process
    for chunk in chunks:
        chunk.page_content = clean_text(chunk.page_content)

    return chunks



# 3. VECTOR DB (Persistent Chroma)
def create_vector_db(chunks):

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    # If DB already exists
    if os.path.exists(PERSIST_DIR):
        print("Loading existing Chroma DB...")
        vector_db = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embeddings,
            persist_directory=PERSIST_DIR
        )
    else:
        print("Creating new Chroma DB...")
        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            collection_name=COLLECTION_NAME,
            persist_directory=PERSIST_DIR
        )
        vector_db.persist()

    return vector_db


# Groq Runnable
def groq_runnable(prompt_value):
    role_map = {
        "human": "user",
        "ai": "assistant",
        "system": "system"
    }

    messages = [
        {"role": role_map.get(msg.type, msg.type), "content": msg.content}
        for msg in prompt_value.messages
    ]

    result = call_groq(messages)
    return result


# 4. BUILD RETRIEVAL CHAIN
def build_chain(vector_db):

    custom_llm = RunnableLambda(groq_runnable)

    prompt = ChatPromptTemplate.from_template("""
        You are a helpful assistant.
        Answer ONLY from the given context.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """)

    retriever = vector_db.as_retriever()

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | custom_llm
    )

    return chain


# 5. PIPELINE
def create_chatbot(pdf_path):

    docs = load_pdf(pdf_path)
    chunks = split_docs(docs)

    vector_db = create_vector_db(chunks)

    chain = build_chain(vector_db)

    return chain




chain = create_chatbot("python.pdf")

while True:
    query = input("Ask about the PDF: ")
    if query:
        response = chain.invoke(query)
        print("Response from AI:", response)
