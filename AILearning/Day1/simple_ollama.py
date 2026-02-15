from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Explain LLMs in simple terms'}
    ]
)

print(response['message']['content'])