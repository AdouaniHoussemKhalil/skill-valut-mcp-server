from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv
import os
from typing import List, Dict

load_dotenv()

mcp = FastMCP(os.environ["APP_NAME"],host=os.environ["HOST"],port=os.environ["PORT"])
tavily_api_key = os.environ['TAVILY_API_KEY']
print(tavily_api_key)
web_search_client = TavilyClient(api_key=tavily_api_key)
import requests

@mcp.tool()
def web_search(query: str) -> List[Dict]:
    """
    Search the web for the given query.
    Args:
        query (str): The search query.
    Returns:
        List[Dict]: The search results.
    """
    try:    
        response = web_search_client.search(query)
        return response.get("results", [])
    except:
        return "No results found"



if __name__ == "__main__":
        mcp.run(transport="sse") 


