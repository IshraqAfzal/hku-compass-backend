import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .courses_job import general_courses_job

class DataJob:
  def __init__(self, logger, db):
    self.logger = logger
    self.db = db
    self.scheduler = AsyncIOScheduler()
    self.setup()

  def setup(self):
    self.logger.info("Setting up jobs")
    # self.scheduler.add_job(general_courses_job, 'cron', month='8-9', hour='7,19', minute='0', args=(self.logger, self.db))
    # self.scheduler.add_job(my_weekly_job, 'cron', month='8-9', day_of_week=0, hour=12, args=('value1', 'value2'))

  def run(self):
    self.logger.info("Running jobs")
    # self.scheduler.start()