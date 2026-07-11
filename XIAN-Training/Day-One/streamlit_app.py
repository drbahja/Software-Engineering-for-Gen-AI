"""
First AI Agent — DeepSeek edition (Streamlit web version)
=========================================================
Same agent as first_agent.py, but with a simple web interface.

Run with:
    streamlit run streamlit_app.py
"""

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, SystemMessage

# --- Setup -----------------------------------------------------------
load_dotenv()
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

# --- UI --------------------------------------------------------------
st.title("My First AI Agent (DeepSeek + LangChain)")

st.write("### Ask a Question")
question = st.text_input(
    "Enter your question:",
    "Who was the first computer scientist?",
)

if st.button("Run Query"):
    if not deepseek_key:
        st.error("DEEPSEEK_API_KEY not found. Copy .env.example to .env and add your key.")
    else:
        model = ChatDeepSeek(
            api_key=deepseek_key,
            model="deepseek-chat",
            temperature=0.7,
        )
        with st.spinner("The agent is thinking..."):
            messages = [
                SystemMessage(content="You are a helpful Computer Science assistant named Rob."),
                HumanMessage(content=question),
            ]
            res = model.invoke(messages)
        st.write("### Final Answer")
        st.markdown(res.content)  # .content — the original code passed the whole object (bug)
