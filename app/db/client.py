
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from .schemas.professors import professors_validator
from .schemas.courses import courses_validator
import ultraimport
logs = ultraimport('__dir__/../logs/logger.py')
logger = logs.get_logger()

class MongoDBClient:
  def __init__(self):
    self.uri = os.getenv("MONGODB_URI")
    self.client = MongoClient(self.uri, server_api=ServerApi('1'))
    self.connection_status = False
    self.db = os.getenv("DB")
    self.connect()
    self.add_schemas()

  def __del__(self):
    self.close()

  def connect(self):
    try:
      self.client.admin.command('ping')
      logger.info("Pinged the deployment. Successfully connected to MongoDB.")
      self.connection_status = True
    except Exception as e:
      logger.error("Error in connecting to MongoDB. Error: " + str(e))
      self.connection_status = False

  def close(self):
    self.client.close()
    logger.info("Database connection closed.")

  def add_schemas(self):
    db = self.client[self.db]

    try:
      res = db.command("collMod", "professors", validator = professors_validator)
      if (not res["ok"]):
        logger.error("Error in adding schema to professors collection. MongoDB responsed with ok = 0.0")
    except Exception as e:
        logger.error("Error in adding schema to professors collection. Error: " + str(e))

    try:
      res = db.command("collMod", "courses", validator = courses_validator)
      if (not res["ok"]):
        logger.error("Error in adding schema to courses collection. MongoDB responsed with ok = 0.0")
    except Exception as e:
        logger.error("Error in adding schema to courses collection. Error: " + str(e))

  def bulk_write(self, collection, array_of_operations):
    db = self.client[self.db]
    try:
      col = db[collection]
    except Exception as e:
      logger.error("Could not find collection " + collection + " in Database: primary. Error: " + str(e))
      return False
    try:
      col.bulk_write(array_of_operations)
      logger.info("Bulk writing to collection: " + collection + " completed successfully.")
      return True
    except Exception as e:
      logger.error("Error while bulk writing to collection: " + collection + " in Database: primary. Error: " + str(e))
      return False