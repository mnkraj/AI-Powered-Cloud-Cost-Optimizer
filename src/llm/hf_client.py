import requests
import os


def call_llm(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}
    payload = {"messages": [{"role": "user","content": prompt}],"model": os.getenv("HF_MODEL")}
    print("Calling LLM API...")
    response = requests.post(f"{os.getenv('HF_API_BASE_URL')}", headers=headers, json=payload)
    response = response.json()
    # response.raise_for_status()
    print("LLM API call successful.")
    return response["choices"][0]["message"]
