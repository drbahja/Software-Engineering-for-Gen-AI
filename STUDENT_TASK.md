# Student Task — Upgrade Your First Agent

You have run the agent and noticed its biggest weakness: **it has no memory**. Each message you send is a brand-new conversation.

## Your task (45–60 min)

### Part 1 — Give the agent memory ⭐

Modify `run_agent()` in `first_agent.py` so the agent remembers the conversation:

1. Before the loop, create a `history` list starting with a `SystemMessage` (invent your own persona — a travel guide, a Python tutor, a Xi'an local expert…).
2. Each turn, append the user's `HumanMessage` to `history` and send the **whole list** to `first_agent()`.
3. Append the model's reply (`AIMessage`) to `history` too.

**Test:** tell the agent your name, then ask "What is my name?" — it must answer correctly.

*Hint:* `from langchain_core.messages import AIMessage`

### Part 2 — Make it yours ⭐⭐

Pick **one**:

- **Translator agent:** system prompt makes it always reply in both English and Chinese.
- **Temperature experiment:** add a way for the user to change `temperature`, and show how answers differ at 0 vs 1.3.
- **Reasoning model:** switch the model to `deepseek-reasoner` and compare its answers on a maths puzzle with `deepseek-chat`.

### Part 3 (bonus) — Web memory ⭐⭐⭐

The Streamlit app also forgets everything. Use `st.session_state` to store the history list and turn `streamlit_app.py` into a real chatbot (`st.chat_input` and `st.chat_message` will help).

## Rules

- Use the DeepSeek API key given by the instructor — do not share it outside the class, and never commit `.env` to git.
- Work in pairs is allowed; be ready to demo your agent in 2 minutes.

## What you'll be assessed on

Does memory work? Is the system prompt creative? Can you explain **every line** you changed?
