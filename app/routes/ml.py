from fastapi import APIRouter, Request
from bson import ObjectId

router = APIRouter(
  prefix="/ml",
  tags=["Machine Learning"]
)



@router.post("/sort-by-relevance-for-course")
async def sort_by_relevance_for_course(request: Request):
    form_data = await request.form()
    course_code = form_data.get("COURSE_CODE")
    reviews = form_data.get("REVIEWS")
    course = request.app.state.db.find('courses', {"COURSE_CODE" : course_code})
    if len(course) != 1:
        return {'data' : reviews}
    description = course[0]["DESCRIPTION"]
    sorted_reviews = request.app.state.models.relevance.sort_texts_on_relevance(description, reviews)
    return {'data' : sorted_reviews}