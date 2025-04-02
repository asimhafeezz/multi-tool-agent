# MultiTool Agent

**MultiTool Agent** is an intelligent assistant application that leverages LangChain, LLaMA 3.1 (via Ollama), and Streamlit to provide users with concise and context-aware answers. It integrates multiple tools—weather reporting, news retrieval, and real-time web search—to deliver accurate and timely information through a user-friendly interface.

### [Demo](https://drive.google.com/file/d/1dnC65mhOuzHT3ojbk7h_9o3UWl_IAN-Q/view?usp=sharing)

---

## Tools
- 🌦️ **Weather Tool** – Get current weather in any city
- 📰 **News Tool** – Fetch recent news headlines
- 🔎 **WebSearch Tool** – Perform general web searches using Serper.dev

---

## Features

- **Multi-Tool Integration**: Uses specialized tools for weather, news, and general web search.
- **Local LLM Support**: Powered by LLaMA 3.1 via Ollama for running models locally.
- **Function-Based Agent**: Implements LangChain's `OpenAIFunctionsAgent` for structured reasoning and tool calling.
- **Memory Management**: Tracks conversational history using LangChain's buffer memory.
- **Interactive Interface**: Built with Streamlit to provide a lightweight and accessible frontend.

---

## 🤖 LLM Model Used
This agent uses LLaMA 3.1, which is served locally via Ollama. Make sure [Ollama](https://ollama.com/) is running and the model is installed:

```bash
ollama run llama3.1
```

---

### 1.	Clone the repository

```bash
git clone [https://github.com/your-username/multi-tool-agent.git](https://github.com/asimhafeezz/multi-tool-agent.git)
cd multi-tool-agent
```

### 2.	Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3.	Install dependencies

```bash
pip install -r requirements.txt
```

### 4.	Run the app

```bash
streamlit run app.py
```

Made with ❤️ by Asim
