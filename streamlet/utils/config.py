import os
from dotenv import load_dotenv

# Automatically load environment variables from the .env file
load_dotenv()

# Get the environment variables (Make sure .env is correctly placed)
WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
WATSONX_URL = os.getenv("WATSONX_URL")
WATSONX_MODEL_ID = os.getenv("WATSONX_MODEL_ID")

# Optional: Debug print to check loading
if not all([WATSONX_API_KEY, WATSONX_PROJECT_ID, WATSONX_URL, WATSONX_MODEL_ID]):
    print("❌ One or more WatsonX environment variables are missing.")
else:
    print("✅ IBM WatsonX config loaded successfully.")
