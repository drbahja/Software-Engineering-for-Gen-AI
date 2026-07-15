import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Load environment variables from .env file
load_dotenv()

deepseek_key = os.getenv("DEEPSEEK_API_KEY")
if not deepseek_key:
    raise ValueError("DEEPSEEK_API_KEY not found. Copy .env.example to .env and add your key.")

llm_name = "deepseek-chat"
model = ChatDeepSeek(api_key=deepseek_key, model=llm_name, temperature=0)

# read csv file (path relative to this script, so it works from any directory)
DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "salaries_2023.csv")
df = pd.read_csv(DATA_PATH)
# Fill missing values per column type: 0 for numbers, "Unknown" for text.
# (A blanket fillna(0) puts ints inside text columns, which breaks/crashes
# the Arrow conversion Streamlit uses to render dataframes.)
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(0)
df = df.fillna("Unknown")

agent = create_pandas_dataframe_agent(
    llm=model,
    df=df,
    verbose=True,
    # Use DeepSeek's native tool calling instead of fragile ReAct text parsing
    agent_type="tool-calling",
    # If the model still produces unparseable output, retry instead of crashing
    agent_executor_kwargs={"handle_parsing_errors": True},
    # This is the key argument that unlocks Python REPL calls
    allow_dangerous_code=True,
)

# then let's add some prefix and suffix prompts
CSV_PROMPT_PREFIX = """
First set the pandas display options to show all the columns,
get the column names, then answer the question.
"""

CSV_PROMPT_SUFFIX = """
- **ALWAYS** before giving the Final Answer, try another method.
Then reflect on the answers of the two methods you did and ask yourself
if it answers correctly the original question.
If you are not sure, try another method.
FORMAT 4 FIGURES OR MORE WITH COMMAS.
- If the methods tried do not give the same result,reflect and
try again until you have two methods that have the same result.
- If you still cannot arrive to a consistent result, say that
you are not sure of the answer.
- If you are sure of the correct answer, create a beautiful
and thorough response using Markdown.
- **DO NOT MAKE UP AN ANSWER OR USE PRIOR KNOWLEDGE,
ONLY USE THE RESULTS OF THE CALCULATIONS YOU HAVE DONE**.
- **ALWAYS**, as part of your "Final Answer", explain how you got
to the answer on a section that starts with: "\n\nExplanation:\n".
In the explanation, mention the column names that you used to get
to the final answer.
"""

st.title("This is our first agent")

st.write("### Dataset Preview")
st.write(df.head())

# User input for the question
st.write("### Ask a Question")
question = st.text_input(
    "Enter your question about the dataset:",
    "Which grade has the highest average base salary, and compare the average female pay vs male pay?",
)

# Run the agent and display the result
if st.button("Run Query"):
    QUERY = CSV_PROMPT_PREFIX + question + CSV_PROMPT_SUFFIX
    with st.spinner("Agent is thinking..."):
        res = agent.invoke(QUERY)
    st.write("### Final Answer")
    st.markdown(res["output"])
