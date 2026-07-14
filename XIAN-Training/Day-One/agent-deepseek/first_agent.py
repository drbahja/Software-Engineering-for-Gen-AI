"""
First AI Agent — DeepSeek edition (CLI version)
================================================
A minimal LLM-powered agent built with LangChain, connected to DeepSeek.

Uses LangChain's dedicated DeepSeek integration (ChatDeepSeek), which
talks to DeepSeek's API directly.

Run step by step in VS Code (see README.md) or run the whole file:
    python first_agent.py
"""

# ------------------------------------------------------------------
# STEP 1 — Imports
# ------------------------------------------------------------------
import os

from dotenv import load_dotenv                      # reads the .env file
from langchain_deepseek import ChatDeepSeek         # DeepSeek chat client
from langchain_core.messages import HumanMessage, SystemMessage

# ------------------------------------------------------------------
# STEP 2 — Load the API key from the .env file
# ------------------------------------------------------------------
load_dotenv()
deepseek_key = os.getenv("DEEPSEEK_API_KEY")

if not deepseek_key:
    raise ValueError("DEEPSEEK_API_KEY not found. Copy .env.example to .env and add your key.")

# ------------------------------------------------------------------
# STEP 3 — Create the model
# ------------------------------------------------------------------
# Models: "deepseek-chat" (general) or "deepseek-reasoner" (reasoning).
llm_name = "deepseek-chat"

model = ChatDeepSeek(
    api_key=deepseek_key,
    model=llm_name,
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
    """Send messages to the model and return the response."""
    res = model.invoke(messages)
    return res


# ------------------------------------------------------------------
# STEP 6 — An interactive chat loop
# ------------------------------------------------------------------
def run_agent():
    print("Simple AI Agent (DeepSeek): Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("AI Agent is thinking...")
        messages = [HumanMessage(content=user_input)]
        response = first_agent(messages)
        print(f"AI Agent: {response.content}")


# ------------------------------------------------------------------
# STEP 7 — Entry point
# ------------------------------------------------------------------
if __name__ == "__main__":
    run_agent()
