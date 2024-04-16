from fastapi import APIRouter, Request
from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Any

router = APIRouter(
  prefix="/ml",
  tags=["Machine Learning"]
)

@router.get("/get-n-recommended-courses-from-uba")
async def get_n_recommended_courses_from_uba(request : Request, course_code = "COMP3322", n : int = 5):
  rec_courses = request.app.state.models.uba.give_recommendations(course_code, n)
  return rec_courses

@router.get("/get-n-recommended-courses-from-recommender-engine")
async def get_n_recommended_courses_from_uba(request : Request, difficulty : float = 1, usefulness : float = 5, grading : float = 5, workload : float = 1, n : int = 5):
  preferences = {
    "DIFFICULTY" : difficulty,
    "USEFULNESS" : usefulness,
    "GRADING" : grading,
    "WORKLOAD" : workload
  }
  rec_courses = request.app.state.models.recommendation_engine.find_closest_courses(preferences, n)
  for course in rec_courses:
    del course["TNL"]
    course["RATING"] /= float(course["RATING_COUNT"])
    course["USEFULNESS"] /= float(course["RATING_COUNT"])
    course["GRADING"] /= float(course["RATING_COUNT"])
    course["WORKLOAD"] /= float(course["RATING_COUNT"])
    course["DIFFICULTY"] /= float(course["RATING_COUNT"])
  return rec_courses

reviews_test = [{
  "COURSE_CODE": "COMP3322",
  "USER_ID": "5f94a577fcaee5e5f36dc0f1",
  "PROF_IDS": ["00000061746374616d5f6373"],
  "COMMENT": "This is test comment " + str(i),
  "RATING": 2,
  "DIFFICULTY": 1,
  "GRADING": 5,
  "USEFULNESS": 5,
  "WORKLOAD": 1,
  "IS_VERIFIED": False,
  "YEAR": "2023-24",
  "SEM": "1",
  "HELPFUL" : 10,
  "NOT_HELPFUL" : 10,
} for i in range(5)]

reviews_model_test = {
  "COURSE_CODE" : "COMP3322",
  "REVIEWS" : reviews_test
}

class ReviewModel(BaseModel):
  _id : Optional[Any] = None
  COMMENT : str
  COURSE_CODE : Optional[str] = None
  DATETIME  : Optional[Any] = None
  USER_ID : Optional[str] = None
  RATING : Optional[float] = None
  DIFFICULTY : Optional[float] = None
  ENGAGEMENT : Optional[float] = None
  CLARITY : Optional[float] = None
  PROF_IDS : Optional[List[str]] = None
  PROF_ID : Optional[str] = None
  PROF_ID_NAME_MAP : Optional[Any] = None
  PROF_NAME : Optional[str] = None
  GRADING : Optional[float] = None
  USEFULNESS : Optional[float] = None
  WORKLOAD : Optional[float] = None
  IS_VERIFIED : Optional[bool] = None
  YEAR : Optional[str] = None
  SEM : Optional[str] = None
  HELPFUL : Optional[int] = None
  NOT_HELPFUL : Optional[int] = None
  USER_DEPARTMENT : Optional[str] = None
  USER_FACULTY : Optional[str] = None
  USER_PROFILE_PIC : Optional[str] = None


class ReviewsModel(BaseModel):
  COURSE_CODE : str
  REVIEWS : List[ReviewModel]
  model_config = ConfigDict(
    json_schema_extra={
      "example": reviews_model_test
    },
  )

@router.post("/sort-by-relevance-for-course")
async def sort_by_relevance_for_course(request : Request, data : ReviewsModel):
  data = BaseModel.model_dump(data)
  course = request.app.state.db.find_one("courses", {"COURSE_CODE" : data["COURSE_CODE"]})
  description = course["COURSE_DESCRIPTION"] if "COURSE_CODE" in course else "This is a course description."
  sorted_reviews = request.app.state.models.relevance.sort_texts_on_relevance(description, data["REVIEWS"])
  return sorted_reviews