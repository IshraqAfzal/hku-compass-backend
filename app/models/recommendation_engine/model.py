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
        "DIFFICULTY" : course["DIFFICULTY"],
        "GRADING" : course["GRADING"],
        "USEFULNESS" : course["USEFULNESS"],
        "WORKLOAD" : course["WORKLOAD"]
      }
    closest_courses = []
    for course, scores in courses_data.items():
        distance = math.sqrt(sum((preferences[metric] - scores[metric]) ** 2 for metric in preferences))
        closest_courses.append((course, distance))
    closest_courses.sort(key=lambda x: x[1])
    result = [course[0] for course in closest_courses[:n]] if n <= len(closest_courses) - 1 else closest_courses
    ret = []
    for r in result:
      ret.append({
        "COURSE_CODE" : r.split("_")[0],
        "COURSE_TITLE" : r.split("_")[1]
      })
    return ret



