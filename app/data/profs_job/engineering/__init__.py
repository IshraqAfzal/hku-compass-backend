from fastapi import APIRouter
from selenium import webdriver
from ....utils.data.create_driver import create_driver
from .cs import router as csRouter, collect as csCollect

router = APIRouter(
  prefix="/engineering",
  tags=["engineering"]
)

router.include_router(csRouter)

def job(db, logger):
  logger.info("ENGG Job: Starting ENGG Job.")
  driver = create_driver()
  csCollect(db, logger, driver)
