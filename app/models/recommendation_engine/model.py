import math, json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

class RecommendationEngine():
  def __init__(self, db) -> None:
    self.db = db
  
  def load_course_data(self):
    courses = self.db.find_all('courses')
    return courses

  def find_closest_courses(self, preferences, n):
    courses = self.load_course_data()
    courses_data = {}
    for course in courses:
      courses_data[course["COURSE_CODE"] + "_" + course["COURSE_TITLE"]] = {
        "DIFFICULTY" : course["DIFFICULTY"] / course["RATING_COUNT"],
        "GRADING" : course["GRADING"] / course["RATING_COUNT"],
        "USEFULNESS" : course["USEFULNESS"] / course["RATING_COUNT"],
        "WORKLOAD" : course["WORKLOAD"] / course["RATING_COUNT"]
      }
    closest_courses = []
    for course, scores in courses_data.items():
        distance = math.sqrt(sum((preferences[metric] - scores[metric]) ** 2 for metric in preferences))
        closest_courses.append((course, distance))
    closest_courses.sort(key=lambda x: x[1])
    selected_courses = [course[0] for course in closest_courses[:n]] if n <= len(closest_courses) - 1 else closest_courses
    selected_course_codes = [course.split("_")[0] for course in selected_courses]
    return_courses = [course for course in courses if course["COURSE_CODE"] in selected_course_codes]
    return return_courses

