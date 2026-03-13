import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_vectorstore(pdf_path):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(documents)

    embeddings = load_embeddings()

    vectorstore = FAISS.from_documents(split_docs, embeddings)

    st.session_state.vectorstore = vectorstore

def get_relevant_docs(query):

    vectorstore = st.session_state.get("vectorstore", None)

    if vectorstore is None:
        print("Vectorstore is None")
        return []

    docs = vectorstore.similarity_search(query, k=3)

    return [doc.page_content for doc in docs]