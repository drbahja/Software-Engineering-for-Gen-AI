# My First AI Agent — DeepSeek + LangChain

A minimal AI agent built with LangChain, connected to **DeepSeek** (works in China, no VPN needed). Two versions: a command-line chat (`first_agent.py`) and a web app (`streamlit_app.py`).

## What changed from the original OpenAI version?

The code now uses LangChain's dedicated DeepSeek integration:

| | Before (OpenAI) | After (DeepSeek) |
|---|---|---|
| API key | `OPENAI_API_KEY` | `DEEPSEEK_API_KEY` |
| Model | `gpt-3.5-turbo` | `deepseek-chat` |
| Client class | `ChatOpenAI` (`langchain-openai`) | `ChatDeepSeek` (`langchain-deepseek`) |

Everything else (LangChain, messages, the agent loop) stays the same. Libraries were also updated from LangChain 0.1.x (2024) to the current 0.3+ series, and unused packages (pyodbc, pandas, SQLAlchemy…) were removed.

---

## Setup (do this once)

### 1. Get the code

```bash
git clone https://github.com/drbahja/Software-Engineering-for-Gen-AI.git
cd Software-Engineering-for-Gen-AI/XIAN-Training/Day-One
```

Or download the ZIP from GitHub (green **Code** button → Download ZIP) and unzip it.

### 2. Open in VS Code

`File → Open Folder…` → select the `first_agent_deepseek` folder.

### 3. Create a virtual environment

Open the VS Code terminal (`Ctrl+`` ` or `Terminal → New Terminal`):

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` at the start of the terminal line. If VS Code asks "select this environment for the workspace?" → click **Yes**.

### 4. Install libraries

```bash
pip install -r requirements.txt
```

> In China, if pip is slow, use the Tsinghua mirror:
> `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 5. Add your API key

Copy `.env.example` to a new file called `.env`, then paste the key your instructor gave you:

```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx
```

⚠️ Never share this key or push `.env` to GitHub (`.gitignore` already blocks it).

---

## Running the code step by step (in VS Code)

Open `first_agent.py`. The file is organised in 7 numbered steps. You can run pieces of it interactively: select some lines and press **Shift+Enter** ("Run Selection in Python Terminal"), or use `# %%` cells with the Jupyter extension.

**Step 1 — Imports.** `ChatDeepSeek` is LangChain's client for the DeepSeek API. `HumanMessage` / `SystemMessage` are how LangChain represents chat roles.

**Step 2 — Load the key.** `load_dotenv()` reads `.env` and `os.getenv` pulls the key into a variable. Keys live in `.env`, never in code.

**Step 3 — Create the model.** `ChatDeepSeek` talks to `https://api.deepseek.com` by default. `temperature=0.7` controls creativity (0 = deterministic, ~1.3 = very creative).

**Step 4 — One call.** Uncomment the two lines and run them:

```python
res = model.invoke(messages)
print(res.content)
```

A `SystemMessage` sets the assistant's personality ("your name is Rob"); the `HumanMessage` is the user question. `.invoke()` sends both and returns an `AIMessage` — the text lives in `.content`.

**Step 5 — The agent function.** Wrapping the call in `first_agent()` — the model plus the logic around it is the beginning of an "agent".

**Step 6 — Chat loop.** `run_agent()` keeps asking for input until you type `exit`. Notice: each turn sends **only the newest message** — the agent has **no memory**. Ask "My name is Li" then "What's my name?" to prove it. (Fixing this is your task — see `STUDENT_TASK.md`.)

**Step 7 — Run everything:**

```bash
python first_agent.py
```

### The web version

```bash
streamlit run streamlit_app.py
```

Browser opens at `http://localhost:8501`. Same agent, with a text box and button instead of the terminal.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Is `(.venv)` active? Re-run step 3–4. |
| `DEEPSEEK_API_KEY not found` | The file must be named exactly `.env` (not `env.txt`), in the project folder. |
| `AuthenticationError 401` | Key typed wrong — no spaces or quotes around it. |
| `streamlit: command not found` | `pip install streamlit` inside the active venv. |
| pip very slow | Use the Tsinghua mirror (see step 4). |
