import os

from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware
import pydantic
from dotenv import load_dotenv  
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(pydantic.BaseModel):
    text: str


@app.post("/generate")
async def chat(request: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-pro-preview",
            contents=request
        )
        
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))