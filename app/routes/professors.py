from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
from ..utils.datetime.hk_time_now import hk_time_now
from bson import ObjectId
from pydantic import BaseModel, ConfigDict
from typing import List, Any

router = APIRouter(
  prefix="/professors",
  tags=["Professors"]
)

@router.get("/get-all")
async def get_all(request: Request):
  professors = request.app.state.db.find_all("professors")
  for professor in professors:
    professor["RATING"] /= professor["RATING_COUNT"]
    professor["CLARITY"] /= professor["RATING_COUNT"]
    professor["ENGAGEMENT"] /= professor["RATING_COUNT"]
  return professors

@router.get("/get")
async def get(request: Request, prof_id = 'atctam_cs'):
  professor = request.app.state.db.find_one("professors", {"PROF_ID" : create_objectid(prof_id)})
  if "PROF_ID" in professor:
    professor["RATING"] /= float(professor["RATING_COUNT"])
    professor["CLARITY"] /= float(professor["RATING_COUNT"])
    professor["ENGAGEMENT"] /= float(professor["RATING_COUNT"])
  return professor

@router.get("/get-history")
async def get(request: Request, prof_id = "Anthony T.C. Tam"):
  history = request.app.state.db.find_all("course_history")
  history = [his for his in history if (prof_id in his["INSTRUCTORS_PLACEHOLDER"])]
  return history

@router.get("/get-reviews")
async def get_reviews(request: Request, prof_id = "atctam_cs"):
  reviews = request.app.state.db.find("prof_reviews", {"PROF_ID" : create_objectid(prof_id)})
  reviews = [review for review in reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  for review in reviews:
    if review["COURSE_CODE"] == "COMP3322":
      prof = request.app.state.db.find_one("professors", {"PROF_ID" : create_objectid("atctam_cs")})
      review["PROF_NAME"] = prof["FULLNAME"]
    review["USER_DEPARTMENT"] = "Computer Science"
    review["USER_FACULTY"] = "Engineering"
    review["USER_PROFILE_PIC"] = "/user-profile-pics/profile-pic.svg"
  return reviews

@router.get("/get-reviews-by-course")
async def get_reviews_by_course(request: Request, course_code = "COMP3322"):
  reviews = request.app.state.db.find("prof_reviews", {"COURSE_CODE" : course_code})
  reviews = [review for review in reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  for review in reviews:
    if review["COURSE_CODE"] == "COMP3322":
      prof = request.app.state.db.find_one("professors", {"PROF_ID" : create_objectid("atctam_cs")})
      review["PROF_NAME"] = prof["FULLNAME"]
    review["USER_DEPARTMENT"] = "Computer Science"
    review["USER_FACULTY"] = "Engineering"
    review["USER_PROFILE_PIC"] = "/user-profile-pics/profile-pic.svg"
  return reviews

@router.get("/get-reviews-by-user")
async def get_reviews_by_user(request: Request, course_code = "COMP3322", user_id = "5f94a577fcaee5e5f36dc0f1"):
  reviews = request.app.state.db.find("prof_reviews", {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  reviews = [review for review in reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  for review in reviews:
    if review["COURSE_CODE"] == "COMP3322":
      prof = request.app.state.db.find_one("professors", {"PROF_ID" : create_objectid("atctam_cs")})
      review["PROF_NAME"] = prof["FULLNAME"]
    review["USER_FACULTY"] = "Engineering"
    review["USER_DEPARTMENT"] = "Computer Science"
    review["USER_PROFILE_PIC"] = "/user-profile-pics/profile-pic.svg"
  return reviews

review_model_test = {
  "COURSE_CODE": "COMP3322",
  "USER_ID": "5f94a577fcaee5e5f36dc0f1",
  "PROF_ID": "00000061746374616d5f6373",
  "COMMENT": "This is a test comment",
  "RATING": 2,
  "CLARITY": 1,
  "ENGAGEMENT": 5,
  "IS_VERIFIED": False,
  "YEAR": "2023-24",
  "SEM": "1"
}

class ReviewModel(BaseModel):
  COURSE_CODE : str
  USER_ID : str
  PROF_ID : str
  COMMENT : str
  RATING : float 
  CLARITY : float
  ENGAGEMENT : float 
  IS_VERIFIED : bool 
  YEAR : str 
  SEM : str
  model_config = ConfigDict(
    arbitrary_types_allowed=True,
    json_encoders={ObjectId: str},
    json_schema_extra={
      "example": review_model_test
    },
  )

@router.post("/create-or-update-review")
async def create_or_update_review(request: Request, data : ReviewModel):
  given_review = BaseModel.model_dump(data)
  given_review["DATETIME"] = hk_time_now()
  given_review["USER_ID"] = ObjectId(given_review["USER_ID"])
  given_review["PROF_ID"] = ObjectId(given_review["PROF_ID"])
  review_from_collection = request.app.state.db.find_one("prof_reviews", {"COURSE_CODE" : given_review["COURSE_CODE"], "USER_ID" : given_review["USER_ID"], "PROF_ID" : given_review["PROF_ID"]})
  rating_count_inc = 0
  if "COURSE_CODE" not in review_from_collection:
    review_from_collection = {
      "RATING" : 0,
      "CLARITY": 0,
      "ENGAGEMENT" : 0
    }
    rating_count_inc = 1
  prof_update_obj = {"$inc" : {
    "RATING" : given_review["RATING"] - review_from_collection["RATING"],
    "CLARITY" : given_review["CLARITY"] - review_from_collection["CLARITY"],
    "ENGAGEMENT" : given_review["ENGAGEMENT"] - review_from_collection["ENGAGEMENT"],
    "RATING_COUNT" : rating_count_inc
  }}
  success_review = request.app.state.db.update_one("prof_reviews", {"COURSE_CODE" : given_review["COURSE_CODE"], "USER_ID" : given_review["USER_ID"], "PROF_ID" : given_review["PROF_ID"]}, given_review, True)
  success_prof = request.app.state.db.update_one_with_custom_fields("professors", {"PROF_ID" : given_review["PROF_ID"]}, prof_update_obj) if success_review else False
  return success_prof and success_review

@router.delete("/delete-review")
async def delete_review(request: Request, id : str):
  review = request.app.state.db.find_one("prof_reviews", {"_id" : ObjectId(id)})
  success_review = request.app.state.db.delete_one("prof_reviews", {"_id" : ObjectId(id)})
  prof_update_obj = {"$inc" : {
    "RATING" : 0 - review["RATING"],
    "CLARITY" : 0 - review["CLARITY"],
    "ENGAGEMENT" : 0 - review["ENGAGEMENT"],
    "RATING_COUNT" : 0 - 1
  }}
  success_prof = request.app.state.db.update_one_with_custom_fields("professors", {"PROF_ID" : review["PROF_ID"]}, prof_update_obj) if success_review else False
  return success_prof and success_review