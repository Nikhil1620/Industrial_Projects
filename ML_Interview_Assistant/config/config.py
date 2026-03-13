import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# -------------------------------
# API KEYS
# -------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------------
# MODEL CONFIGURATION
# -------------------------------

LLM_MODEL_NAME = "llama3-8b-8192"

# -------------------------------
# EMBEDDING MODEL
# -------------------------------

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# -------------------------------
# RAG SETTINGS
# -------------------------------

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K_RESULTS = 3

# -------------------------------
# FILE STORAGE
# -------------------------------

DOCUMENT_FOLDER = "documents"