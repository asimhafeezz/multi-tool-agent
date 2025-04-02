import requests
from langchain.agents import Tool
from config import NEWSAPI_API_KEY

def get_news(topic: str) -> str:
    """Get latest news on a topic.
    
    Args:
        topic (str): The topic to search for news about
        
    Returns:
        str: News headlines or error message
    """
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWSAPI_API_KEY}&pageSize=3&sortBy=publishedAt"
    try:
        res = requests.get(url).json()
        if res.get("status") != "ok":
            return "Could not fetch news."
        articles = res.get("articles", [])
        if not articles:
            return f"No news found on '{topic}'."
        headlines = "\n\n".join([f"- {a['title']} ({a['source']['name']})" for a in articles])
        return f"Latest news on '{topic}':\n\n{headlines}"
    except Exception as e:
        return f"News API error: {e}"

# news tool
news_tool = Tool(
    name="News",
    func=get_news,
    description="Use to get latest news headlines. Input should be a topic or keyword."
)