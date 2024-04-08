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
    success = request.app.state.db.update_one('users', {"USER_ID" : ObjectId(user_id)}, new_data, True)
    return {'data' : success}

@router.post("/set-transcript-info")
async def set_transcript_info(request: Request):
    form_data = await request.form()
    user_id = form_data.get("USER_ID")
    pdf_file = form_data.get("PDF")
    parsed_pdf = request.app.state.models.transcript_parser(pdf_file)
    courses = parsed_pdf["Courses"]
    data = {
      "COURSE_HISTORY" : [{
        "COURSE_CODE" : course['Course Code'].split(" ")[0] + course['Course Code'].split(" ")[1],
        "YEAR" : course["Term"].split(" ")[0],
        "SEM" : course["Grade"],
        "IS_REVIEWED" : False
      } for course in courses]
    }
    success = request.app.state.db.update_one('users', {"USER_ID" : ObjectId(user_id)}, data)
    return {"data" : {
        "PARSED_DATA": parsed_pdf,
        "SUCCESS": success
    }}