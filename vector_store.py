from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


def create_vectorstore(documents):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=128,       # reduce size to avoid hitting 512 limit
    chunk_overlap=16
    )
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(texts, embeddings, persist_directory="chroma_db")
    vectordb.persist()
    return vectordb
