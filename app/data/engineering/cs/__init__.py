from fastapi import APIRouter
from .professors import collect_prof_data
from .db import write

router = APIRouter(
  prefix="/cs",
  tags=["cs"]
)

last_profs = []

def collect(db, logger, driver, inject):
  global last_profs
  logger.info("CS Job: Starting CS Job.")
  prof_data = collect_prof_data(driver, logger)
  last_profs = prof_data
  data = {}
  data['profs'] = prof_data
  # Push to db
  # write(db, logger, prof_data)


@router.get("/profs", tags=["profs"])
async def profs():
    return last_profs


