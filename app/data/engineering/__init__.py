from fastapi import APIRouter
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pathlib
from .cs import router as csRouter, collect as csCollect

router = APIRouter(
  prefix="/engineering",
  tags=["engineering"]
)

router.include_router(csRouter)

def job(db, logger, inject):
  logger.info("ENGG Job: Starting ENGG Job.")
  options = webdriver.ChromeOptions()
  options.add_argument("--enable-javascript")
  options.add_argument("--headless")
  options.add_argument("--disable-logging")
  options.add_argument("--no-sandbox")
  path = str(pathlib.Path().resolve()) + "/data/drivers/chromedriver"
  service = webdriver.ChromeService(executable_path = path)
  driver = webdriver.Chrome(options = options, service=service)
  csCollect(db, logger, driver, inject)
