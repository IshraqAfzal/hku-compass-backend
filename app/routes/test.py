from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/test",
  tags=["Testing"]
)

@router.get("/hello-world")
async def hello_world():
  return {'hello' : 'world'}

@router.get("/db-connectivity")
async def db_connectivity(request: Request):
  return {'connection_status' : request.app.state.db.connection_status}