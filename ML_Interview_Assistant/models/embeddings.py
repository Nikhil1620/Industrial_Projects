import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Global variable
vectorstore = None


@st.cache_resource
def load_embeddings():
    """Load embedding model only once"""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_vectorstore(pdf_path):
    global vectorstore

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    texts = [doc.page_content for doc in documents]

    embeddings = load_embeddings()

    vectorstore = FAISS.from_texts(texts, embeddings)