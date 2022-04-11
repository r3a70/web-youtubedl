from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.routers import youtube

app = FastAPI()

app.include_router(youtube.router)

templates = Jinja2Templates(directory="frontend")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

