import random
import requests
from fastapi import APIRouter
from pymongo import UpdateOne
from ...utils.data.create_driver import create_driver
from ...utils.data.strm import calculate_strm
from ...constants.data import acad_groups
from .token import get_bearer_token
from .parser import parse_json

router = APIRouter(
  prefix="/courses_job",
  tags=["courses"]
)

last_courses = []
last_subclasses = []
last_sftl = []
last_enrollments = []

async def general_courses_job(logger, db):
  token = None
  last_courses = []
  last_subclasses = []
  last_sftl = []
  last_enrollments = []

  try:
    logger.info('Starting courses job')
    for acad_group in acad_groups:
      logger.info("Current ACAD_GROUP: " + str(acad_group))
      
      token, res_json = get_response(logger, acad_group, token)
      if res_json is None:
        logger.error("API Call responsed with None data")
        continue
      logger.info("Response Received")
      
      courses, subclasses, sftl, enrollments = parse_json(res_json, logger)
      logger.info("JSON Parsed")
      
      courses_update_operations = [
        UpdateOne(
            {"COURSE_ID": obj["COURSE_ID"]},
            {"$set": obj},
            upsert=True
        )
        for obj in courses
      ]
      subclasses_update_operations = [
        UpdateOne(
            {"SUBCLASS_ID": obj["SUBCLASS_ID"]},
            {"$set": obj},
            upsert=True
        )
        for obj in subclasses
      ]
      sftl_update_operations = [
        UpdateOne(
            {"STRM": obj["STRM"], "COURSE_CODE" : obj["COURSE_ID"]},
            {"$set": obj},
            upsert=True
        )
        for obj in sftl
      ]
      enrollments_update_operations = [
        UpdateOne(
            {"SUBCLASS_ID": obj["SUBCLASS_ID"], "COURSE_ID" : obj["COURSE_ID"]},
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
      logger.info("Bulk writing done")
      
      last_courses += random.sample(courses, 5) if len(courses) > 5 else courses
      last_subclasses += random.sample(subclasses, 5) if len(subclasses) > 5 else subclasses
      last_sftl += random.sample(sftl, 5) if len(sftl) > 5 else sftl
      last_enrollments += random.sample(enrollments, 5) if len(enrollments) > 5 else enrollments
    logger.info("Courses job finished.")
    return True
  except Exception as ex:
    logger.error(ex)
    return False

def get_response(logger, acad_group, bearer_token):
  token = get_bearer_token(create_driver(), logger) if bearer_token is None else bearer_token
  endpoint = "https://class-planner.hku.hk/api/subclasses/precise?strm=" + calculate_strm() + "&weekdays=Mon-AM,Mon-PM,Tues-AM,Tues-PM,Wed-AM,Wed-PM,Thurs-AM,Thurs-PM,Fri-AM,Fri-PM,Sat-AM,Sat-PM,Sun-AM,Sun-PM&commonCore=false&acadGroup=" + acad_group
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


@router.get("/courses", tags=["courses"])
async def courses():
    return last_courses

@router.get("/subclasses", tags=["subclasses"])
async def subclasses():
    return last_subclasses

@router.get("/sftl", tags=["sftl"])
async def sftl():
    return last_sftl

@router.get("/enrollments", tags=["enrollments"])
async def enrollments():
    return last_enrollments


