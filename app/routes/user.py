from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
from bson import ObjectId

router = APIRouter(
  prefix="/user",
  tags=["User Data"]
)

@router.get("/get-user-data")
async def get_user_data(request: Request, user_id = Query(0)):
  data = request.app.state.db.find('users', {"USER_ID" : user_id})
  return {'data' : data}

@router.post("/update-user-data")
async def update_user_data(request: Request):
    form_data = await request.form()
    user_id = form_data.get("USER_ID")
    new_data = form_data.get("NEW_DATA")
    success = request.app.state.db.update_one('users', {"USER_ID" : ObjectId(user_id)}, new_data)
    return {'data' : success}

@router.post("/extract-transcript-info")
async def extract_transcript_info(request: Request):
    pdf_file = await request.form()
    pdf_text = request.app.state.models.transcript_parser(pdf_file)
    transcript_info = extract_transcript_info(pdf_text)
    return transcript_info