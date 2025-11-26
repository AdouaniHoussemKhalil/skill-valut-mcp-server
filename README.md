MCP Server – GitHub Release & Web Search Automation

This project provides an MCP (Model Context Protocol) server built with FastMCP.
It exposes tools that allow clients to:

🔎 1. Perform Web Searches

Uses the Tavily API to search the web and return structured results through the web_search MCP tool.

🚀 2. Check Latest GitHub Releases

The github_search tool retrieves the latest release of major technologies (React, .NET, Python, Java, Go, Rust, Elixir, TypeScript, etc.) using GitHub’s public API.

🔔 3. Notify Users Only Once Per Release

The server includes a lightweight SQLite database that stores:

Known releases

Notification history (user → release)

This ensures:

Users are not notified multiple times for the same release

New releases are automatically saved in the database

Each user receives notifications only when necessary

🗄️ Database Structure

The server automatically initializes two tables:

releases — stores all processed GitHub releases

notifications — ensures unique user notifications

MCP Server – GitHub Release & Web Search Automation

This project provides an MCP (Model Context Protocol) server built with FastMCP.
It exposes tools that allow clients to:

🔎 1. Perform Web Searches

Uses the Tavily API to search the web and return structured results through the web_search MCP tool.

🚀 2. Check Latest GitHub Releases

The github_search tool retrieves the latest release of major technologies (React, .NET, Python, Java, Go, Rust, Elixir, TypeScript, etc.) using GitHub’s public API.

🔔 3. Notify Users Only Once Per Release

The server includes a lightweight SQLite database that stores:

Known releases

Notification history (user → release)

This ensures:

Users are not notified multiple times for the same release

New releases are automatically saved in the database

Each user receives notifications only when necessary

🗄️ Database Structure

The server automatically initializes two tables:

releases — stores all processed GitHub releases

notifications — ensures unique user notifications

🚀 Installation & Setup
Follow these steps to set up the MCP server environment using uv and Node.js:

1. Initialize a new Python project
uv init

2. Install required Python dependencies
uv add python-dotenv
uv add tavily-python
uv add mcp.server.fastmcp
uv add "mcp[cli]"

3. (Optional) Inspect your MCP server using the MCP Inspector

This tool helps debug and visualize MCP tools during development:

npx @modelcontextprotocol/inspector@0.16

4. Run the MCP server

Make sure your environment variables are configured in a .env file, then start the server:

uv run mcp-server-http.py
(Replace mcp-server-http.py with the actual filename of your MCP server script)
