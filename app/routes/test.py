from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/test",
  tags=["test"]
)

@router.get("/helloWorld")
async def helloworld():
  return {'hello' : 'world'}

@router.get("/dbConnectivity")
async def dbconnectivity(request: Request):
  return {'connection_status' : request.app.state.db.connection_status}