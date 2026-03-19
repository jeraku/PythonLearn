import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def run_agent():
    async with sse_client("http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print("-", tool.name)

            result = await session.call_tool(
                name="add_numbers",
                arguments={"a": 5, "b": 7}
            )

            print("\nResult:", result.content)

asyncio.run(run_agent())