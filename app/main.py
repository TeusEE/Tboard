from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.on_event("startup")
def on_startup():
    from .models.models import create_db_and_tables
    create_db_and_tables()


from .page import router as page_router
from .application import router as app_router
app.include_router(page_router)
app.include_router(app_router)