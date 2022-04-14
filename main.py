from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.routers import downloader

app = FastAPI()

app.include_router(downloader.router)

templates = Jinja2Templates(directory="frontend")
app.mount("/frontend/", StaticFiles(directory="frontend/"), name="static")


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

