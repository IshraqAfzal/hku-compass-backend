from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
from ..utils.typing.objectid import PyObjectId
from bson import ObjectId
from pydantic import BaseModel, ConfigDict
from typing import List, Any
from pymongo import UpdateOne
import datetime, random

# TODO: For reviews
# TODO: aggregate and fetch user data
# TODO: aggregate and fetch instructor details
# TODO: pur routes and types in seperate folders and different files

# TODO: For create-reviews
# TODO: maybe use upserted_id instead?
# TODO: use HTTP errors for all
# TODO: use a pipeline instead

router = APIRouter(
  prefix="/courses",
  tags=["Courses"]
)

@router.get("/get-all")
async def get_all(request: Request):
  courses = request.app.state.db.find_all("courses")
  for course in courses:
    del course["TNL"]
    course["RATING"] /= float(course["RATING_COUNT"])
    course["USEFULNESS"] /= float(course["RATING_COUNT"])
    course["GRADING"] /= float(course["RATING_COUNT"])
    course["WORKLOAD"] /= float(course["RATING_COUNT"])
    course["DIFFICULTY"] /= float(course["RATING_COUNT"])
  return courses

@router.get("/get")
async def get(request: Request, course_code = "COMP3322"):
  course = request.app.state.db.find_one("courses", {"COURSE_CODE" : course_code})
  course["RATING"] /= float(course["RATING_COUNT"])
  course["USEFULNESS"] /= float(course["RATING_COUNT"])
  course["GRADING"] /= float(course["RATING_COUNT"])
  course["WORKLOAD"] /= float(course["RATING_COUNT"])
  course["DIFFICULTY"] /= float(course["RATING_COUNT"])
  return course

@router.get("/get-subclasses")
async def get_subclasses(request: Request, course_code = "COMP3322"):
  subclasses = request.app.state.db.find("subclasses", {"COURSE_CODE" : course_code})
  enrollments = request.app.state.db.find("enrollments", {"COURSE_CODE" : course_code})
  data = {
    "SUBCLASSES" : subclasses,
    "ENROLLMENTS" : enrollments
  }
  return data

@router.get("/get-sftl")
async def get_sftl(request: Request, course_code = "COMP3322"):
  sftl = request.app.state.db.find("sftl", {"COURSE_CODE" : course_code})
  return sftl

@router.get("/get-history")
async def get_history(request: Request, course_code = "COMP3322"):
  history = request.app.state.db.find("course_history", {"COURSE_CODE" : course_code})
  return history

@router.get("/get-all-history")
async def get_history(request: Request):
  history = request.app.state.db.find_all("course_history")
  return history

@router.get("/get-reviews")
async def get_reviews(request: Request, course_code = "COMP3322"):
  reviews = request.app.state.db.find("course_reviews", {"COURSE_CODE" : course_code})
  reviews = [review for review in reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  for review in reviews:
    if course_code == "COMP3322":
      review["PROF_ID_NAME_MAP"] = {
        "PROF_ID" : create_objectid("atctam_cs"),
        "PROF_NAME" : "Tam Tat Chun"
      }
    review["USER_DEPARTMENT"] = "Computer Science"
    review["USER_FACULTY"] = "Engineering"
    review["USER_PROFILE_PIC"] = "/user-profile-pics/profile-pic.svg"
  return reviews

@router.get("/get-reviews-by-user")
async def get_reviews_by_user(request: Request, course_code = "COMP3322", user_id = "5f94a577fcaee5e5f36dc0f1"):
  reviews = request.app.state.db.find("course_reviews", {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  reviews = [review for review in reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  for review in reviews:
    if course_code == "COMP3322":
      review["PROF_ID_NAME_MAP"] = {
        "PROF_ID" : create_objectid("atctam_cs"),
        "PROF_NAME" : "Tam Tat Chun"
      }
  return reviews

@router.get("/get-all-reviews-by-user-and-course-code")
async def get_all_reviews_by_user_and_course_code(request: Request, course_code = "COMP3322", user_id = "5f94a577fcaee5e5f36dc0f1"):
  course_reviews = request.app.state.db.find("course_reviews", {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  course_reviews = [review for review in course_reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  prof_reviews = request.app.state.db.find("prof_reviews", {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  prof_reviews = [review for review in prof_reviews if review["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(review["COMMENT"]))]
  return {"COURSE_REVIEWS" : course_reviews, "PROF_REVIEWS" : prof_reviews}

review_model_test = {
  "COURSE_CODE": "COMP3322",
  "USER_ID": "5f94a577fcaee5e5f36dc0f1",
  "PROF_IDS": ["00000061746374616d5f6373"],
  "COMMENT": "This is a test comment",
  "RATING": 2,
  "DIFFICULTY": 1,
  "GRADING": 5,
  "USEFULNESS": 5,
  "WORKLOAD": 1,
  "IS_VERIFIED": False,
  "YEAR": "2023-24",
  "SEM": "1"
}

class ReviewModel(BaseModel):
  COURSE_CODE : str
  USER_ID : str
  PROF_IDS : List[str]
  COMMENT : str
  RATING : float 
  DIFFICULTY : float
  GRADING : float 
  USEFULNESS : float
  WORKLOAD : float 
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
  given_review["DATETIME"] = datetime.datetime.now()
  given_review["USER_ID"] = ObjectId(given_review["USER_ID"])
  given_review["PROF_IDS"] = [ObjectId(prof_id) for prof_id in given_review["PROF_IDS"]]
  review_from_collection = request.app.state.db.find_one("course_reviews", {"COURSE_CODE" : given_review["COURSE_CODE"], "USER_ID" : given_review["USER_ID"]})
  rating_count_inc = 0
  if "COURSE_CODE" not in review_from_collection:
    review_from_collection = {
      "RATING" : 0,
      "USEFULNESS" : 0,
      "GRADING": 0, 
      "WORKLOAD" : 0, 
      "DIFFICULTY": 0, 
    }
    rating_count_inc = 1
  course_update_obj = {"$inc" : {
    "RATING" : given_review["RATING"] - review_from_collection["RATING"],
    "USEFULNESS" : given_review["USEFULNESS"] - review_from_collection["USEFULNESS"],
    "GRADING" : given_review["GRADING"] - review_from_collection["GRADING"],
    "WORKLOAD" : given_review["WORKLOAD"] - review_from_collection["WORKLOAD"],
    "DIFFICULTY" : given_review["DIFFICULTY"] - review_from_collection["DIFFICULTY"],
    "RATING_COUNT" : rating_count_inc
  }}
  success_review = request.app.state.db.update_one("course_reviews", {"COURSE_CODE" : given_review["COURSE_CODE"], "USER_ID" : given_review["USER_ID"]}, given_review, True)
  success_course = request.app.state.db.update_one_with_custom_fields("courses", {"COURSE_CODE" : given_review["COURSE_CODE"]}, course_update_obj) if success_review else False
  return success_course and success_review

@router.delete("/delete-review")
async def delete_review(request: Request, id : str):
  review = request.app.state.db.find_one("course_reviews", {"_id" : ObjectId(id)})
  success_review = request.app.state.db.delete_one("course_reviews", {"_id" : ObjectId(id)})
  course_update_obj = {"$inc" : {
    "RATING" : 0 - review["RATING"], 
    "USEFULNESS" : 0 - review["USEFULNESS"], 
    "GRADING": 0 - review["GRADING"], 
    "WORKLOAD" : 0 - review["WORKLOAD"], 
    "DIFFICULTY": 0 - review["DIFFICULTY"], 
    "RATING_COUNT" : 0 - 1, 
  }}
  success_course = request.app.state.db.update_one_with_custom_fields("courses", {"COURSE_CODE" : review["COURSE_CODE"]}, course_update_obj) if success_review else False
  return success_course and success_review