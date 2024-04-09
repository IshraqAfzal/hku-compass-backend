from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
import random
from bson import ObjectId

router = APIRouter(
  prefix="/courses",
  tags=["Courses"]
)

@router.get("/get-all")
async def get_all(request: Request):
  data = request.app.state.db.find_all('courses')
  for i in data:
    del i["ACAD_GROUP"]
    del i["TNL"]
  return {'data' : data}

@router.get("/get")
async def get(request: Request, course_code = Query(0)):
  data = request.app.state.db.find_one('courses', {"COURSE_CODE" : course_code})
  del data['ACAD_GROUP']
  return {'data' : data}

@router.get("/get-subclasses")
async def get_subclasses(request: Request, course_code = Query(0)):
  subclasses = request.app.state.db.find('subclasses', {"COURSE_CODE" : course_code})
  enrollments = request.app.state.db.find('enrollments', {"COURSE_CODE" : course_code})
  data = {
    "subclasses" : subclasses,
    "enrollments" : enrollments
  }
  return {'data' : data}

@router.get("/get-enrollments")
async def get_enrollments(request: Request, course_code = Query(0)):
  data = request.app.state.db.find('enrollments', {"COURSE_CODE" : course_code})
  return {'data' : data}

@router.get("/get-sftl")
async def get_sftl(request: Request, course_code = Query(0)):
  data = request.app.state.db.find('sftl', {"COURSE_CODE" : course_code})
  return {'data' : data}

@router.get("/get-history")
async def get_history(request: Request, course_code = Query(0)):
  data = request.app.state.db.find('course_history', {"COURSE_CODE" : course_code})
  return {'data' : data}

@router.get("/get-reviews")
async def get_reviews(request: Request,course_code = Query(0)):
  data = request.app.state.db.find('course_reviews', {"COURSE_CODE" : course_code})
  data = [ datum for datum in data if datum["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(datum["COMMENT"]))]
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_code == "COMP3322":
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
  return {'data' : data}

@router.get("/get-reviews-by-user")
async def get_reviews_by_user(request: Request, course_code = Query(0), user_id = Query(1)):
  data = request.app.state.db.find('course_reviews', {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  data = [ datum for datum in data if datum["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(datum["COMMENT"]))]
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_code == "COMP3322":
      prof = request.app.state.db.find_one('professors', {"PROF_ID" : create_objectid('atctam_cs')})
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
  return {'data' : data}

@router.get("/get-all-reviews-by-user-and-course-code")
async def get_all_reviews_bu_user_and_course_code(request: Request, course_code = Query(0), user_id = Query(1)):
  course_reviews = request.app.state.db.find('course_reviews', {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  course_reviews = [ datum for datum in course_reviews if datum["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(datum["COMMENT"]))]
  for datum in course_reviews:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_code == "COMP3322":
      prof = request.app.state.db.find_one('professors', {"PROF_ID" : create_objectid('atctam_cs')})
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
  prof_reviews = request.app.state.db.find('prof_reviews', {"COURSE_CODE" : course_code, "USER_ID" : ObjectId(user_id)})
  prof_reviews = [ datum for datum in prof_reviews if datum["COMMENT"] is not None and (not request.app.state.models.spam.is_spam(datum["COMMENT"]))]
  for datum in prof_reviews:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_code == "COMP3322":
      prof = request.app.state.db.find_one('professors', {"PROF_ID" : create_objectid('atctam_cs')})
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
  return {'data' : {
    "COURSE_REVIEWS" : course_reviews,
    "PROF_REVIEWS" : prof_reviews
  }}

@router.post("/create-review")
async def create_review(request: Request):
    form_data = await request.form()
    user_id = form_data.get("USER_ID")
    course_code = form_data.get("COURSE_CODE")
    prof_id = form_data.get("PROF_ID")
    new_data = form_data.get("NEW_DATA")
    success = request.app.state.db.update_one('course_reviews', {"USER_ID" : ObjectId(user_id), "COURSE_CODE" : course_code, "PROF_ID" : ObjectId(prof_id)}, new_data, True)
    return {'data' : success}

@router.delete("/delete-review")
async def delete_review(request: Request, id = Query(0)):
  success = request.app.state.db.delete_one('course_reviews', {"_id" : ObjectId(id)})
  return {'data' : success}