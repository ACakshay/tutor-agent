from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path

# Create router for UI endpoints
ui_router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"


templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@ui_router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Serve the main index page for user setup using Jinja2 template
    """
    html_path = TEMPLATES_DIR / "index.html"
    if html_path.exists():
        return templates.TemplateResponse("index.html", {"request": request})
    else:
        raise HTTPException(status_code=404, detail="index.html not found")


@ui_router.get("/chat", response_class=HTMLResponse)
async def chat_page():
    """
    Serve the chat interface page
    """
    try:
        html_path = TEMPLATES_DIR / "chat.html"
        if html_path.exists():
            with open(html_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            return HTMLResponse(content=html_content)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error loading chat page: {str(e)}"
        )
