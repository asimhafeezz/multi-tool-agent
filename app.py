import streamlit as st
from langchain.agents import AgentExecutor
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage
from tools import tools
from config import MAX_ITERATIONS, VERBOSE, LLM_MODEL, LLM_TEMPERATURE

llm = ChatOllama(model=LLM_MODEL, temperature=LLM_TEMPERATURE)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

system_message = """You are a smart and concise assistant with access to several tools.
- Use the Weather tool for weather questions
- Use the News tool for recent news headlines
- Use the WebSearch tool for general information needs

Answer directly and avoid unnecessary explanations.
Complete the task efficiently without getting stuck in loops."""

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=system_message),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

# agent
agent = OpenAIFunctionsAgent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# agent executor
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=VERBOSE,
    handle_parsing_errors=True,
    max_iterations=MAX_ITERATIONS
)

# Streamlit app
st.set_page_config(page_title="MultiTool Agent", layout="centered")
st.title("MultiTool Agent")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask me anything...", key="input")

if user_input:
    st.session_state.history.append(("You", user_input))
    with st.spinner("Thinking..."):
        try:
            response = agent_executor.invoke(input=user_input)
            st.session_state.history.append(("MultiTool Agent", response["output"]))
        except TypeError as e:
            st.error(f"Agent error: {str(e)}")
            # Fallback method if the first approach fails
            try:
                response = agent_executor({"input": user_input})
                st.session_state.history.append(("MultiTool Agent", response["output"]))
            except Exception as fallback_error:
                st.error(f"Fallback error: {str(fallback_error)}")
                st.session_state.history.append(("MultiTool Agent", "Sorry, I encountered an error processing your request."))

for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")