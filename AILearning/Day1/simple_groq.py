TOKEN = "<>"
from groq import Groq
import os

client = Groq(api_key=TOKEN)

while True:
    question = input("Enter your question: ")
    messages = [
        {"role": "system", "content": "You are a senior DevOps engineer"},
        {"role": "user", "content": f"{question}"}
    ]


    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    print(response.choices[0].message.content)