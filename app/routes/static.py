from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(
  prefix="/static",
  tags=["Static"]
)

@router.get("/upload-transcript-info")
async def serve_html():
  return FileResponse("app/static/upload_transcript_info.html")