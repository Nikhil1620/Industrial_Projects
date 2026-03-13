import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Load environment variables from .env
load_dotenv()

def get_chatgroq_model():
    """Initialize and return the Groq chat model"""
    try:
        groq_model = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant",
            temperature=0
        )
        return groq_model

    except Exception as e:
        raise RuntimeError(f"Failed to initialize Groq model: {str(e)}")


def get_toolbound_model():
    return get_chatgroq_model()