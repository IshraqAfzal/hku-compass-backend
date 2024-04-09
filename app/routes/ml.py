from fastapi import APIRouter, Request, Query

router = APIRouter(
  prefix="/ml",
  tags=["Machine Learning"]
)

@router.post("/sort-by-relevance-for-course")
async def sort_by_relevance_for_course(request: Request):
    form_data = await request.form()
    course_code = form_data.get("COURSE_CODE")
    reviews = form_data.get("REVIEWS")
    course = request.app.state.db.find_one('courses', {"COURSE_CODE" : course_code})
    description = course["DESCRIPTION"]
    sorted_reviews = request.app.state.models.relevance.sort_texts_on_relevance(description, reviews)
    return {"data" : sorted_reviews}

@router.get("/get-n-recommended-courses-from-uba")
async def get_n_recommended_courses_from_uba(request: Request, course_code = Query(0), n = Query(1)):
  course = request.app.state.db.find_one('courses', {"COURSE_CODE" : course_code})
  courses = request.app.state.db.find_all('courses')
  rec_courses = request.app.state.models.uba.give_recommendations(course["COURSE_TITLE"], courses, n) if "COURSE_TITLE" in course else []
  return {"data" : rec_courses}