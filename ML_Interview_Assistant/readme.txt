# ML Interview Assistant 🤖

A Streamlit-based chatbot that helps users prepare for Machine Learning interviews. It leverages **RAG (Retrieval-Augmented Generation)** with uploaded resumes and 
an LLM model (Groq API) to answer questions about ML concepts, algorithms, and personalized resume insights.

---

## Features

- **General ML Q&A** – Ask questions about algorithms, models, and concepts.
- **Resume-based assistance** – Upload a resume (PDF) and ask questions about skills, experience, or education.
- **Dynamic response modes** – Choose between concise or detailed answers.
- **RAG-powered** – Uses embeddings and vectorstore to retrieve relevant context from uploaded PDFs.
- **Clean chat interface** – Built with Streamlit for an interactive experience.

---

## Project Structure
project/
├── config/
│ └── config.py # API keys and environment variables
├── models/
│ ├── llm.py # LLM (Groq) models
│ └── embeddings.py # RAG embedding and FAISS vectorstore
├── utils/ # Helper functions (RAG, tools, etc.)
├── app.py # Main Streamlit app
├── requirements.txt # Required Python packages
└── .gitignore # Ignore .env, caches, temp files


---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

Add your API key

Create a .env file in the root of the project:

Run the app

streamlit run app.py

Usage

Open the Streamlit web app.

Ask general ML questions or upload a resume (PDF) for RAG-based insights.

Choose between Concise or Detailed responses from the sidebar.

Clear chat and uploaded data using the sidebar button when needed.

Requirements

Python 3.10+

Streamlit

LangChain and compatible packages

HuggingFace Transformers & Sentence Transformers

FAISS (via LangChain Community modules)

See requirements.txt for the full list.

Notes

The Groq API key is required for LLM interactions.

Resume PDFs are processed with FAISS embeddings for fast retrieval.

Ensure .env file is present locally for the app to access API keys.
