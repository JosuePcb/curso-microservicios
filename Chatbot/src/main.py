import os

from fastapi import FastAPI # type: ignore
from dotenv import load_dotenv  
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

@app.post("/chat")
def chat(message: str):
    response = client.chat(
        model="gemini-3.1-pro-preview",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return {"response": response}
