from fastapi import FastAPI, Request, status, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from backend.routers import downloader
from backend.db import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    openapi_url=None,
    redoc_url=None,
    docs_url=None
)

app.include_router(downloader.router)

templates = Jinja2Templates(directory="frontend")
app.mount("/frontend/", StaticFiles(directory="frontend/"), name="static")


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def read_item(request: Request, db: Session = Depends(database.get_db)):
    ip = request.client.host
    db_query = db.query(models.Visit).filter(models.Visit.visited == ip).first()
    if not db_query:
        new_visit = models.Visit(visited=ip)
        db.add(new_visit)
        db.commit()
    return templates.TemplateResponse("index.html", {"request": request, "ip": ip})

