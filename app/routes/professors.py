from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
import random

router = APIRouter(
  prefix="/professors",
  tags=["Professors"]
)

@router.get("/get-all")
async def get_all(request: Request):
  data = request.app.state.db.find_all('professors')
  return {'data' : data}

@router.get("/get")
async def get(request: Request, prof_code = Query(0)):
  data = request.app.state.db.find('courses', {"PROF_ID" : create_objectid(prof_code)})
  return {'data' : data}

@router.get("/get-reviews")
async def get_reviews(request: Request, prof_code = Query(0)):
  data = request.app.state.db.find('prof_reviews', {"PROF_ID" : create_objectid(prof_code)})
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if datum['COURSE_ID'] == create_objectid("030837"):
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
    pass
  return {'data' : data}

@router.get("/get-reviews-by-course")
async def get_reviwews_by_course(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('prof_reviews', {"COURSE_ID" : create_objectid(course_id)})
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_id == "030837":
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
    pass
  return {'data' : data}

@router.get("/get-reviews-by-user")
async def get_reviews_by_user(request: Request, course_id = Query(0), user_id = Query(1)):
  data = request.app.state.db.find('prof_reviews', {"COURSE_ID" : create_objectid(course_id), "USER_ID" : ObjectId(user_id)})
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_id == "030837":
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
    pass
  return {'data' : data}

