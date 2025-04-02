
import os
from dotenv import load_dotenv

# envs
load_dotenv()

# API Keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# LLM Settings
LLM_MODEL = "llama3.1"
LLM_TEMPERATURE = 0.3

# Agent Settings
MAX_ITERATIONS = 3
VERBOSE = True