from fastapi import APIRouter, status, Request
from backend.src import youtube_extractor
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/api/v1/youtube',
    tags=['YouTube']
)


templates = Jinja2Templates(directory="frontend")


@router.get("/", status_code=status.HTTP_200_OK)
async def download_from_youtube(url: str, request: Request):
    video_info = await youtube_extractor.yt_extractor(url)
    return templates.TemplateResponse("youtube.html", {"request": request, "info": video_info})
