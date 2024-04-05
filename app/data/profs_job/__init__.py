from fastapi import APIRouter
from .engineering import router as enggRouter, job as enggJob

router = APIRouter(
  prefix="/profs",
  tags=["Professor Data Collection"]
)
router.include_router(enggRouter)

async def profs_job(db, logger):
  enggJob(db, logger)