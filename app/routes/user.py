from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
from bson import ObjectId
from pydantic import BaseModel, ConfigDict
from typing import Optional, List

router = APIRouter(
  prefix="/user",
  tags=["User Data"]
)

@router.get("/get-user-data")
async def get_user_data(request: Request, email = "test@hku.hk"):
  user = request.app.state.db.find_one('users', {"EMAIL" : email})
  return user

user_model_test = {
  "EMAIL" : "test@hku.hk",
  "IS_ONBOARDED" : False
}

class CourseHistoryModel(BaseModel):
  COURSE_CODE : str
  YEAR : str
  SEM : str
  IS_REVIEWED : bool

class UserUpdateModel(BaseModel):
  EMAIL : str
  FULLNAME : Optional[str] = None
  DEGREE : Optional[str] = None
  YEAR_OF_STUDY : Optional[str] = None 
  MAJORS : Optional[List[str]] = None
  MINORS : Optional[List[str]]  = None
  COURSE_HISTORY : Optional[List[CourseHistoryModel]] = None
  BOOKMARKS : Optional[List[str]] = None
  CART : Optional[List[str]] = None
  IS_ONBOARDED : Optional[bool] = None
  model_config = ConfigDict(
    arbitrary_types_allowed = True,
    json_encoders={ObjectId: str},
    json_schema_extra={
      "example": user_model_test
    },
  )

@router.post("/update-user-data")
async def update_user_data(request: Request, user : UserUpdateModel):
  user = BaseModel.model_dump(user)
  keys = [key for key in user]
  for key in keys:
    if user[key] is None:
      del user[key]
  success = request.app.state.db.update_one('users', {"EMAIL" : user["EMAIL"]}, user)
  return success

@router.post("/get-transcript-info")
async def set_transcript_info(request: Request, user_id):
  pdf_file = await request.form()
  parsed_pdf = request.app.state.models.transcript_parser(pdf_file)
  courses = parsed_pdf["Courses"]
  course_history = {
    "COURSE_HISTORY" : [{
      "COURSE_CODE" : course['Course Code'].split(" ")[0] + course['Course Code'].split(" ")[1],
      "YEAR" : course["Term"].split(" ")[0],
      "SEM" : course["Grade"],
      "IS_REVIEWED" : False
    } for course in courses]
  }
  return {"COURSE_HISTORY": course_history["COURSE_HISTORY"], "SUCCESS": success}