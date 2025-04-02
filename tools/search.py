import requests
from langchain.agents import Tool
from config import SERPER_API_KEY

def serper_search(query: str) -> str:
    """Perform a web search using Serper API.
    
    Args:
        query (str): The search query
        
    Returns:
        str: Search results or error message
    """
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    body = {"q": query}
    try:
        response = requests.post("https://google.serper.dev/search", headers=headers, json=body)
        data = response.json()
        if "error" in data:
            return f"Serper error: {data['error']}"
        results = data.get("organic", [])
        if not results:
            return "No relevant results found."
        summary = "\n\n".join([f"- {r['title']} - {r['snippet']}" for r in results[:3]])
        return f"Top results:\n\n{summary}"
    except Exception as e:
        return f"Error calling Serper: {e}"

# serper tool
serper_tool = Tool(
    name="WebSearch",
    func=serper_search,
    description="Use this to perform a web search when real-time information is needed. Input should be a search query."
)