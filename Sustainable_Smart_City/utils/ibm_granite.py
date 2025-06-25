# utils/ibm_granite.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load WatsonX credentials
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
BASE_URL = os.getenv("WATSONX_URL")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")

def get_iam_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={API_KEY}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return None

def ask_granite(prompt: str) -> str:
    """Basic one-shot prompt (used by eco_tips, kpi, policy, etc.)"""
    token = get_iam_token()
    if not token:
        return "❌ Error: Failed to authenticate with IBM Cloud."

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "model_id": MODEL_ID,
        "input": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.7
        },
        "project_id": PROJECT_ID
    }

    url = f"{BASE_URL}/ml/v1/text/generation?version=2024-05-01"
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()["results"][0]["generated_text"].strip()
        except Exception as e:
            return f"⚠️ Error parsing response: {e}"
    return f"❌ API error: {response.status_code} - {response.text}"

def ask_granite_with_context(question: str, context: str) -> str:
    """Used in chat assistant with file context"""
    full_prompt = f"{context}\n\nAnswer this:\n{question}"
    return ask_granite(full_prompt)
