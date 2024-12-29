from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from .main import templates

router = APIRouter()

@router.get("/main_page", response_class = HTMLResponse)
async def main(req: Request):
    return templates.TemplateResponse(
        request = req, name = "index.html"
    )


@router.get("/login_page", response_class = HTMLResponse)
async def login(req: Request):
    return templates.TemplateResponse(
        request = req, name = "login.html"
    )