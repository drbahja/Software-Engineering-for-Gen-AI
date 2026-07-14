"""
First AI Agent — Local SLM edition (runs on YOUR laptop, no internet needed)
============================================================================
Same agent as the DeepSeek version, but the "brain" is a Small Language
Model served locally by Ollama at http://localhost:11434/v1.

Because Ollama speaks the OpenAI-compatible API, we use LangChain's
ChatOpenAI class and simply point it at our own machine. No API key,
no cloud, no cost — and it works offline.

Before running:
    1. Install Ollama  (https://ollama.com)
    2. ollama pull qwen2.5:1.5b     (or the model that fits your laptop)
    3. python first_agent.py
"""

# ------------------------------------------------------------------
# STEP 1 — Imports
# ------------------------------------------------------------------
import os

from dotenv import load_dotenv                      # reads the .env file
from langchain_openai import ChatOpenAI             # OpenAI-compatible client
from langchain_core.messages import HumanMessage, SystemMessage

# ------------------------------------------------------------------
# STEP 2 — Configuration (no secret key needed for a local model!)
# ------------------------------------------------------------------
load_dotenv()
llm_name = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")   # change model in .env

# ------------------------------------------------------------------
# STEP 3 — Create the model — pointed at YOUR laptop
# ------------------------------------------------------------------
model = ChatOpenAI(
    api_key="ollama",                        # any text works; nothing is sent to the cloud
    model=llm_name,
    base_url="http://localhost:11434/v1",    # Ollama's local API on your machine
    temperature=0.7,
)

# ------------------------------------------------------------------
# STEP 4 — A single call to the model
# ------------------------------------------------------------------
messages = [
    SystemMessage(
        content="You are a helpful assistant who is extremely competent "
                "as a Computer Scientist! Your name is Rob."
    ),
    HumanMessage(content="Who was the very first computer scientist?"),
]

# Uncomment these two lines to test a single call:
# res = model.invoke(messages)
# print(res.content)


# ------------------------------------------------------------------
# STEP 5 — Wrap the call in a function (our "agent")
# ------------------------------------------------------------------
def first_agent(messages):
    """Send messages to the local model and return the response."""
    res = model.invoke(messages)
    return res


# ------------------------------------------------------------------
# STEP 6 — An interactive chat loop
# ------------------------------------------------------------------
def run_agent():
    print(f"Simple AI Agent (local · {llm_name}): Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("AI Agent is thinking (on your laptop!)...")
        messages = [HumanMessage(content=user_input)]
        response = first_agent(messages)
        print(f"AI Agent: {response.content}")


# ------------------------------------------------------------------
# STEP 7 — Entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    run_agent()
