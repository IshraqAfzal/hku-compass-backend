from pymongo import ReplaceOne

def write(db, logger, courses):
  courses_insertion_list = map_courses_insertion_list(courses)
  db.bulk_write("courses", courses_insertion_list)

def map_courses_insertion_list(courses):
  list = []
  for course in courses:
    list.append(course_replace_object(course))
  return list

def course_replace_object(course):
  return ReplaceOne({"code" : course["code"]}, course, upsert=True)