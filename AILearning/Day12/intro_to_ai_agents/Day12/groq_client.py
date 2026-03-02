import os
import requests
import json


def call_groq(messages):
    api_key = "<grok>"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": messages,
        "temperature": 0.0
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    return data["choices"][0]["message"]["content"]