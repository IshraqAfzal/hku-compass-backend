from fastapi import APIRouter, Request, HTTPException
from ..utils.data.create_objectid import create_objectid
from pydantic import BaseModel
from typing import Union

router = APIRouter(
  prefix = "/auth",
  tags = ["Authentication"]
)

@router.get("/does-user-exist")
async def does_user_exist(request : Request, email : str = "test@hku.hk"):
  user = request.app.state.db.find("users", {"EMAIL" : email})
  return len(user) == 1

class LoginModel(BaseModel):
  EMAIL : str
  PASSWORD : str

@router.post("/login")
async def login(data : LoginModel, request : Request):
  data = BaseModel.model_dump(data)
  user = request.app.state.db.find_one("users", {"EMAIL" : data["EMAIL"], "PASSWORD" : data["PASSWORD"]})
  return {"LOGIN_STATUS" : "EMAIL" in user , "USER_DATA" : user}

@router.post("/change-password")
async def change_password(request: Request, data : LoginModel):
  data = BaseModel.model_dump(data)
  success = request.app.state.db.update_one('users', {"EMAIL" : data["EMAIL"]}, {'PASSWORD' : data["PASSWORD"]})
  return success

class RegisterModel(LoginModel):
  FULLNAME : str
  PROFILE_PIC : str

@router.post("/register")
async def register(request: Request, data : RegisterModel):
  user_data = BaseModel.model_dump(data)
  user_data["DEPARTMENT"] = ""
  user_data["FACULTY"] = ""
  user_data["FACULTY"] = ""
  user_data["YEAR_OF_STUDY"] = ""
  user_data["MAJORS"] = []
  user_data["MINORS"] = []
  user_data["DEGREE"] = ""
  user_data["IS_ONBOARDED"] = False
  user_data["COURSE_HISTORY"] = []
  user_data["BOOKMARKS"] = []
  user_data["CART"] = []
  user_data["HELPFUL_REVIEWS"] = []
  user_data["NOT_HELPFUL_REVIEWS"] = []
  success = request.app.state.db.update_one('users', {}, user_data, True)
  return success