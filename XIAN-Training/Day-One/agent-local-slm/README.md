# First Agent — Local SLM Edition (Ollama)

The same first agent, but the model runs **on your own laptop** with [Ollama](https://ollama.com) — free, private, offline.

Full step-by-step instructions: **[Day 2 · Lab Part 5 on the course site](https://drbahja.github.io/Software-Engineering-for-Gen-AI/day2-lab-part5.html)**.

## Quick start

```bash
# 1. Install Ollama from https://ollama.com, then pull a small model:
ollama pull qwen2.5:1.5b

# 2. Set up the project
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# 3. Run
python first_agent.py            # terminal chat
streamlit run streamlit_app.py   # web version
```

No API key needed — the "brain" is on `http://localhost:11434`, your own machine.
