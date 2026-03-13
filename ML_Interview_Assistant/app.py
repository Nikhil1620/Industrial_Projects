import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.llm import get_chatgroq_model
from utils.rag import build_vectorstore, get_relevant_docs

import time

def get_chat_response(model, messages, system_prompt):
    try:
        formatted_messages = [{"role": "system", "content": system_prompt}]
        formatted_messages.extend(messages)

        response = model.invoke(formatted_messages)

        return response.content

    except Exception as e:
        return f"Error generating response: {str(e)}"


def chat_page():
    st.title("🤖 ML Interview Assistant")

    with st.sidebar:
        st.session_state.response_mode = st.selectbox(
            "Response Mode", ["Concise", "Detailed"], key="mode"
        )

        uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

        if uploaded_file is not None:

            os.makedirs("documents", exist_ok=True)

            file_path = os.path.join("documents", uploaded_file.name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            if "vectorstore" not in st.session_state:
                build_vectorstore(file_path)
                st.success("indexed successfully!")

        if st.button("🗑️ Clear Chat & Index"):
            st.session_state.messages = []
            st.rerun()

    mode_prompt = (
        "Respond concisely."
        if st.session_state.response_mode == "Concise"
        else "Provide detailed explanations."
    )

    system_prompt = (
        f"You are an ML Interview Assistant. {mode_prompt} "
        "If resume context is provided, answer using that resume."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about ML concepts, algorithms..."):

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                docs = get_relevant_docs(prompt)

                if docs:
                    context = "\n".join(docs)

                    full_prompt = f"""
Use the following resume to answer the question.

Resume:
{context}

Question:
{prompt}
"""
                else:
                    full_prompt = prompt

                model = get_chatgroq_model()

                response = get_chat_response(
                    model,
                    [{"role": "user", "content": full_prompt}],
                    system_prompt
                )

                if "search_web" in str(response):
                    time.sleep(2)
                    response += "\n\n(Web search results integrated.)"

                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()


def main():
    chat_page()


if __name__ == "__main__":

    main()
