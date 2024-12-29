from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from .main import templates
from .models.models import engine

router = APIRouter()

@router.post("/login_user")
async def login_user(req: Request):
    
    return {"message": "login_user"}