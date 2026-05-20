DAG-> 
Open AI
N8n

Ai Agent 
1) Tools (addition, getweather)
2) Memory (persistent chroma DB) - context window creation
3) Model - Nomic embed text
4) groq API  Open AI model - > Brain
5) 


Latency and cost to get better performance.

DAG architecture (oneway) A->D , no D->A 


1. Foundation model > Brain > (LLM) > Opn AI model
2. Planning module > TASK will be planned > end goal. (chain of thought, tree of thought, heirarichal tree of flow,)
3. Memory module > Short term and long term. (vector DB/Redis - short term)
4. Tools -> Travel Iternary planner [mode of transport, sugestion, timing, weather] > External tools.
5. Learning and reflection > HIL - Human in the loop.

AI agent is not tool calling 
reason : Tool calling - Get weather return weather info only. AI agent will give extra information.

--------------------
**n8n components
chat model
memory, 
Tool output
parser. 




Tools.py:
Addition and getweather. 
memory.py:
persistent chroma DB 
groq client.py:
Open AI model . brain 
Agent.py:
memory, tool > get user input and 


simple reflex agent. 
To run: python main.py

