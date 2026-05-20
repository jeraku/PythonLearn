import os
import requests
from dotenv import load_dotenv
load_dotenv()
import os
def call_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    print(api_key)
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()