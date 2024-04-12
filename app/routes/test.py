from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/test",
  tags=["Testing"]
)

@router.get("/hello-world")
async def hello_world():
  return "Hello World"

@router.get("/db-connectivity")
async def db_connectivity(request: Request):
  return request.app.state.db.connection_status