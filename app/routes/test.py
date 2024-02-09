from fastapi import APIRouter

router = APIRouter(
  prefix="/test",
  tags=["test"]
)

@router.get("/helloworld")
async def helloworld():
  return {'hello' : 'world'}