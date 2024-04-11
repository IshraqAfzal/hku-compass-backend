import random
import requests
from pymongo import UpdateOne
from ...utils.data.create_driver import create_driver
from ...utils.data.strm import calculate_strm
from ...constants.data import acad_groups
from .token import get_bearer_token
from .parser import parse_json

# TODO: Maybe add a toggle for the loggin?

async def general_courses_job(logger, db):
  logger.info('Starting courses job')
  strms = calculate_strm()
  token = None
  last_courses = []
  last_subclasses = []
  last_sftl = []
  last_enrollments = []
  fin = 0
  for strm in strms:
    logger.info("Current STRM: " + str(strm))
    try:
      for acad_group in acad_groups:
        logger.info("Current ACAD_GROUP: " + str(acad_group))
        
        token, res_json = get_response(logger, strm, acad_group, token)
        if res_json is None:
          logger.error("API Call responsed with None data")
          continue
        logger.info("Response Received")
        
        courses, subclasses, sftl, enrollments, history = parse_json(res_json, logger)
        logger.info("JSON Parsed")
        
        courses_update_operations = [
          UpdateOne(
              {"COURSE_CODE": obj["COURSE_CODE"]},
              {"$set": obj},
              upsert=True
          )
          for obj in courses
        ]
        subclasses_update_operations = [
          UpdateOne(
              {"SUBCLASS_CODE": obj["SUBCLASS_CODE"]},
              {"$set": obj},
              upsert=True
          )
          for obj in subclasses
        ]
        sftl_update_operations = [
          UpdateOne(
              {"STRM": obj["STRM"], "COURSE_CODE" : obj["COURSE_CODE"]},
              {"$set": obj},
              upsert=True
          )
          for obj in sftl
        ]
        course_history_operations = [
          UpdateOne(
              {"STRM": obj["STRM"], "COURSE_CODE" : obj["COURSE_CODE"]},
              {"$set": obj},
              upsert=True
          )
          for obj in history
        ]
        enrollments_update_operations = [
          UpdateOne(
              {"SUBCLASS_CODE": obj["SUBCLASS_CODE"]},
              {"$set": obj},
              upsert=True
          )
          for obj in enrollments
        ]

        logger.info("Bulk writing beginning")
        db.bulk_write('courses', courses_update_operations) if len(courses_update_operations) > 0 else None
        db.bulk_write('subclasses', subclasses_update_operations) if len(subclasses_update_operations) > 0 else None
        db.bulk_write('sftl', sftl_update_operations) if len(sftl_update_operations) > 0 else None
        db.bulk_write('enrollments', enrollments_update_operations) if len(enrollments_update_operations) > 0 else None
        db.bulk_write('course_history', course_history_operations) if len(course_history_operations) > 0 else None
        logger.info("Bulk writing done")
        
        last_courses += random.sample(courses, 5) if len(courses) > 5 else courses
        last_subclasses += random.sample(subclasses, 5) if len(subclasses) > 5 else subclasses
        last_sftl += random.sample(sftl, 5) if len(sftl) > 5 else sftl
        last_enrollments += random.sample(enrollments, 5) if len(enrollments) > 5 else enrollments
      fin += 1
    except Exception as ex:
      logger.error(ex)
  if fin == 3:
    logger.info("Courses job finished.")
    return True
  else:
    logger.info("Courses job ran into errors.")
    return False

def get_response(logger, strm, acad_group, bearer_token):
  token = get_bearer_token(create_driver(), logger) if bearer_token is None else bearer_token
  endpoint = "https://class-planner.hku.hk/api/subclasses/precise?strm=" + strm + "&weekdays=Mon-AM,Mon-PM,Tues-AM,Tues-PM,Wed-AM,Wed-PM,Thurs-AM,Thurs-PM,Fri-AM,Fri-PM,Sat-AM,Sat-PM,Sun-AM,Sun-PM&commonCore=false&acadGroup=" + acad_group
  logger.info("Getting Response from endpoint: " + endpoint)
  headers = {"Authorization": token}
  res = requests.get(endpoint, headers=headers)
  data = None
  if res.status_code == 200:
    data = res.json()
  elif res.status_code == 401:
    logger.error("Error in getting Auth Bearer Token")
  else:
    logger.error("Error in fetching from the API, server responded with status " + str(res.status_code))
  return (token, data)


