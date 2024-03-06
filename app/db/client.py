
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os, uuid
from .schemas.professors import professors_validator
from .schemas.courses import courses_validator
from .schemas.prof_reviews import prof_reviews_validator
from .schemas.course_reviews import course_reviews_validator
from .schemas.enrollments import enrollments_validator
from .schemas.sftl import sftl_validator
from .schemas.subclasses import subclasses_validator
from .schemas.users import users_validator
from ..logs.logger import logger
# from logs.logger import logger

class MongoDBClient:
  def __init__(self, name = str(uuid.uuid1)):
    self.name = name
    self.uri = str(os.getenv("MONGODB_URI"))
    self.client = MongoClient(self.uri, server_api=ServerApi('1'))
    self.connection_status = False
    self.db = str(os.getenv("DB"))
    logger.info("Database client " + self.name + ": URI being used is " + str(self.uri))
    logger.info("Database client " + self.name + ": Database being used is " + str(self.db))
    self.connect()

  def __del__(self):
    self.close()

  def connect(self):
    try:
      self.client.admin.command('ping')
      logger.info("Database client " + self.name + ": Pinged the deployment. Successfully connected to MongoDB.")
      self.connection_status = True
      self.add_schemas()
    except Exception as e:
      logger.error("Database client " + self.name + ": Error in connecting to MongoDB. Error: " + str(e))
      self.connection_status = False

  def close(self):
    self.client.close()
    logger.info("Database client " + self.name + ": Database connection closed.")

  def add_schemas(self):
    db = self.client[self.db]

    collection_names = ['course_reviews', 'courses', 'enrollments', 'prof_reviews', 'professors', 'sftl', 'subclasses', 'users']
    collection_validators = [course_reviews_validator, courses_validator, enrollments_validator, prof_reviews_validator, professors_validator, sftl_validator, subclasses_validator, users_validator]
    
    for i, name in enumerate(collection_names):
      try:
        res = db.command("collMod", name, validator = collection_validators[i])
        if (not res["ok"]):
          logger.error("Database client " + self.name + ": Error in adding schema to the " + name + " collection. MongoDB responsed with ok = 0.0")
      except Exception as e:
          logger.error("Database client " + self.name + ": Error in adding schema to the " + name + " collection. Error: " + str(e))

  def bulk_write(self, collection, array_of_operations):
    db = self.client[self.db]
    try:
      col = db[collection]
    except Exception as e:
      logger.error("Database client " + self.name + ": Could not find collection " + collection + " in Database: " + os.getenv('DB') + ". Error: " + str(e))
      return False
    try:
      col.bulk_write(array_of_operations)
      logger.info("Database client " + self.name + ": Bulk writing to collection: " + collection + " completed successfully.")
      return True
    except Exception as e:
      logger.error("Database client " + self.name + ": Error while bulk writing to collection: " + collection + " in Database: " + os.getenv('DB') + ". Error: " + str(e))
      return False