from mcp.server.fastmcp import FastMCP
from mcp.server.stdio import stdio_server

mcp = FastMCP("Local StdIO MCP")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    stdio_server(mcp)