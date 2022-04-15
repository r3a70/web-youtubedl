from fastapi import APIRouter, status, Request, Depends
from backend.src import youtube_extractor, find_url_destination, tiktok_extractor, twitter_extractor
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from backend.db import models, database


router = APIRouter(
    prefix='/api/v1/youtube',
    tags=['YouTube']
)


templates = Jinja2Templates(directory="frontend")


@router.get("/", status_code=status.HTTP_200_OK)
async def download_from_youtube(url: str, request: Request, db: Session = Depends(database.get_db)):

    db_query = db.query(models.Uses).filter(models.Uses.urls == url).first()

    try:
        video_type = await find_url_destination.find(url)
        if video_type is None:
            return RedirectResponse("/")
        elif video_type == "youtube":
            video_info = await youtube_extractor.yt_extractor(url)
        elif video_type == "tiktok":
            video_info = await tiktok_extractor.tk_extractor(url)
        elif video_type == "twitter":
            video_info = await twitter_extractor.tw_extractor(url)
        else:
            return RedirectResponse("/")
    except Exception:
        return RedirectResponse("/")
    if not db_query:
        new_uses = models.Uses(urls=url)
        db.add(new_uses)
        db.commit()
    return templates.TemplateResponse("youtube.html", {"request": request, "info": video_info})


