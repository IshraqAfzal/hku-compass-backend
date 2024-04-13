from fastapi import APIRouter, Request, HTTPException

router = APIRouter(
  prefix="/test",
  tags=["Testing"]
)

@router.get("/hello-world")
async def hello_world():
  return "Hello World!"

@router.get("/db-connectivity")
async def db_connectivity(request: Request):
  return request.app.state.db.connection_status

@router.get("/exception_handling")
async def exception_handling():
  raise Exception("This is a test")

@router.get("/http_exception_handling")
async def exception_handling():
  raise HTTPException("This is a test")