from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

@router.get("/helloWorld")
async def helloworld():
  return {'hello' : 'world'}