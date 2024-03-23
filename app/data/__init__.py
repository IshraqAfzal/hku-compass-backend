from fastapi import APIRouter
from .profs_job import router as profsRouter
from .courses_job import router as coursesRouter

router = APIRouter(
  prefix="/data",
  tags=["data"]
)

router.include_router(profsRouter)
router.include_router(coursesRouter)