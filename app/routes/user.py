from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/user",
  tags=["User Data"]
)

@router.get("/helloWorld")
async def helloworld():
  return {'hello' : 'world'}