import asyncio
import sys
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession

async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            await session.initialize()

            tools = await session.list_tools()
            print("Tools:", tools)

            result = await session.call_tool("add", {"a": 10, "b": 5})
            print("Result:", result)

asyncio.run(main())