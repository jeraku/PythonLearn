import json
from groq_client import call_groq
from tools import add, get_weather
from memory import MemoryManager


class Agent:

    def __init__(self):
        self.memory = MemoryManager(session_id="user1")

        self.tools = {
            "add": add,
            "get_weather": get_weather
        }

    def run1(self, user_input):
        long_term = self.memory.search_long_term(user_input)
        print(long_term)

    def run(self, user_input):

        short_term = self.memory.get_short_term()
        long_term = self.memory.search_long_term(user_input)

        print("Short-Term:", short_term)
        print("Long-Term:", long_term)

        system_prompt = """
        You are an intelligent AI agent with memory.

        Available tools:
            1. add(a: int, b: int)
            2. get_weather(city: str)

        Use past memories if relevant.
        If tool required, respond ONLY in JSON:
        {
            "tool": "tool_name",
            "args": [...]
        }
        """

        messages = [{"role": "system", "content": system_prompt}]

        if long_term:
            memory_context = "\n".join(long_term)
            messages.append({
                "role": "system",
                "content": f"Relevant Past Memory:\n{memory_context}"
            })

        messages.extend(short_term)

        messages.append({"role": "user", "content": user_input})

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
                    "content": f"Tool result: {tool_result}. Provide final answer."
                })

                final_answer = call_groq(messages)
                result = final_answer
            else:
                result = "Tool not found"

        except json.JSONDecodeError:
            result = llm_output

        self.memory.add_short_term("user", user_input)
        self.memory.add_short_term("assistant", result)

        if self.memory.should_store_long_term(user_input):
            self.memory.add_long_term(user_input)

        return result