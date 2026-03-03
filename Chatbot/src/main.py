
import os
import base64
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from google import genai
from google.genai import types


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


class Message(BaseModel):
    role: str
    text: str


class ChatRequest(BaseModel):
    text: str
    history: list[Message] = []


def extract_tokens(response):
    try:
        meta = response.usage_metadata
        return {
            "input_tokens":  meta.prompt_token_count,
            "output_tokens": meta.candidates_token_count,
            "total_tokens":  meta.total_token_count,
        }
    except Exception:
        return {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}


@app.post("/generate")
async def chat(request: ChatRequest):
    try:
        contents = []
        for msg in request.history:
            contents.append(
                types.Content(
                    role=msg.role,
                    parts=[types.Part(text=msg.text)]
                )
            )
        contents.append(
            types.Content(
                role="user",
                parts=[types.Part(text=request.text)]
            )
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents
        )

        return {
            "response": response.text,
            "tokens": extract_tokens(response),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate-with-image")
async def chat_with_image(
    text: str = Form(...),
    file: Optional[UploadFile] = File(None)
):
    try:
        parts = []

        if file:
            file_bytes = await file.read()
            mime_type = file.content_type or "image/jpeg"
            parts.append(
                types.Part(
                    inline_data=types.Blob(
                        mime_type=mime_type,
                        data=file_bytes
                    )
                )
            )

        parts.append(types.Part(text=text))

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[types.Content(role="user", parts=parts)]
        )

        return {
            "response": response.text,
            "tokens": extract_tokens(response),
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))