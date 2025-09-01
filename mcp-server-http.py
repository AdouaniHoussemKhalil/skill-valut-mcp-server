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

@mcp.tool()
def github_search(tech: str, action: str) -> List[Dict]:
    """
    Search GitHub repositories based on technology and action.
    Args:
        tech (str): The technology to search for.
        action (str): The action to perform (e.g., "find", "list").
    Returns:
        List[Dict]: The search results.
    """
    if tech.lower() == "react" :
        url = "https://api.github.com/repos/facebook/react/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
    if tech.lower() == "dotnet" or tech.lower() == ".net":
        url = "https://api.github.com/repos/dotnet/aspnetcore/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []

    if tech.lower() == "python":
        url = "https://api.github.com/repos/python/cpython/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []

    if tech.lower() == "java":
        url = "https://api.github.com/repos/openjdk/jdk/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
    if tech.lower() == "go":
        url = "https://api.github.com/repos/golang/go/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
    if tech.lower() == "rust":
        url = "https://api.github.com/repos/rust-lang/rust/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
    if tech.lower() == "elixir":
        url = "https://api.github.com/repos/elixir-lang/elixir/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
        
    if tech.lower() == "javascript":
        url = "https://api.github.com/repos/javascript/javascript/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []
    if tech.lower() == "typescript":
        url = "https://api.github.com/repos/microsoft/TypeScript/releases/latest"
        res = requests.get(url)
        if res.status_code == 200:
            return [res.json()]
        else:
            return []


if __name__ == "__main__":
        mcp.run(transport="sse") 


