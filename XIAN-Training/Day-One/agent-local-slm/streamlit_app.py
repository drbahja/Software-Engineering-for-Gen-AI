"""
First AI Agent — Local SLM edition (Streamlit web version)
==========================================================
Run with:
    streamlit run streamlit_app.py
Requires Ollama running with your chosen model pulled.
"""

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# --- Setup -----------------------------------------------------------
load_dotenv()
llm_name = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")

model = ChatOpenAI(
    api_key="ollama",
    model=llm_name,
    base_url="http://localhost:11434/v1",
    temperature=0.7,
)

# --- UI --------------------------------------------------------------
st.title("My First AI Agent (Local SLM + LangChain)")
st.caption(f"Model: {llm_name} · running 100% on this laptop via Ollama")

st.write("### Ask a Question")
question = st.text_input(
    "Enter your question:",
    "Who was the first computer scientist?",
)

if st.button("Run Query"):
    with st.spinner("The agent is thinking on your laptop..."):
        messages = [
            SystemMessage(content="You are a helpful Computer Science assistant named Rob."),
            HumanMessage(content=question),
        ]
        try:
            res = model.invoke(messages)
            st.write("### Final Answer")
            st.markdown(res.content)
        except Exception as e:
            st.error(f"Could not reach Ollama. Is it running? Did you pull the model?\n\n{e}")
