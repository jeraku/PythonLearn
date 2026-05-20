import json
import uuid
from groq_client import call_groq
from tools import add, get_weather
from memory import ChromaMemory

class Agent:

    def __init__(self):
        self.memory = ChromaMemory()
        self.tools = {
            "add": add,
            "get_weather": get_weather
        }

    def run(self, user_input):

        context = self.memory.search(user_input)
        print("Retrieved Context:", context)

        system_prompt = """
            You are an AI agent.

            Available tools:
            1. add(a: int, b: int)
            2. get_weather(city: str)

            If a tool is required, respond ONLY in JSON:
            {
            "tool": "tool_name",
            "args": [...]
            }

            Otherwise respond normally.
            """

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context}\n\nUser: {user_input}"}
        ]

        llm_output = call_groq(messages)

        try:
            parsed = json.loads(llm_output)

            tool_name = parsed["tool"]
            args = parsed["args"]

            if tool_name in self.tools:

                tool_result = self.tools[tool_name](*args)

                messages.append({
                    "role": "assistant",
                    "content": llm_output
                })

                messages.append({
                    "role": "user",
                    "content": f"Tool result: {tool_result}\nProvide final answer."
                })

                final_answer = call_groq(messages)

                result = final_answer

            else:
                result = "Tool not found"

        except json.JSONDecodeError:
            result = llm_output

        self.memory.add(f"User: {user_input}")
        self.memory.add(f"Agent: {result}")

        return result
    # SIMPLE REFLEX AGENT