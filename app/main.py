from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.ai_utils import ask_gemini
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
def read_root():
    return {"message": "Hello from Railway"}

@app.post("/generate")
async def generate_content(request: Request):
    body = await request.json()
    prompt = body.get("prompt")
    if not prompt:
        return {"error": "Prompt is required."}

    result = ask_gemini(prompt)
    return {"response": result}
