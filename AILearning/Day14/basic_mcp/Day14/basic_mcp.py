from mcp.server.fastmcp import FastMCP

# Create MCP app directly
mcp = FastMCP("My Simple MCP Server")


@mcp.tool()
async def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
async def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello {name}, welcome to MCP world!"


if __name__ == "__main__":
    mcp.run(transport="sse")