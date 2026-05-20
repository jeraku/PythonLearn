import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq


async def main():

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        groq_api_key="<GROQ_API_KEY>"
    )

    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": ["./local_mcp.py"],
            },
            "search": {
                "transport": "http",
                "url": "https://mcp.tavily.com/mcp/?tavilyApiKey=<TAVILY_API_KEY>",
            }
        }
    )

    tools = await client.get_tools()

    for tool in tools:
        print("Tool:", tool)
        input()

    agent = create_agent(
        llm,
        tools,
        system_prompt="""
            You are a helpful AI assistant.

            When a math calculation is required:
            - ALWAYS use the appropriate tool.
            - Do NOT write the answer yourself.
            """
    )

    math_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "Do a summation of 2 and 3"}
            ]
        }
    )

    search_response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "Give me details on Iran News"}
            ]
        }
    )

    print("Math Response:", math_response)
    print("Search Response:", search_response)


if __name__ == "__main__":
    asyncio.run(main())