from fastapi import APIRouter, Request
from ..utils.data.create_objectid import create_objectid

router = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

@router.post("/login")
async def login(request: Request):
    form_data = await request.form()
    email = form_data.get("EMAIL")
    password = form_data.get("PASSWORD")
    user = request.app.state.db.find_one('users', {"EMAIL" : email, "PASSWORD": password})
    return {"data" : user}

@router.post("/does-user-exist")
async def does_user_exist(request: Request):
    form_data = await request.form()
    email = form_data.get("EMAIL")
    user = request.app.state.db.find('users', {"EMAIL" : email})
    exists = len(user) == 0
    return {"data" : exists}

@router.post("/register")
async def register(request: Request):
    form_data = await request.form()
    user_data = form_data.get('USER_DATA')
    success = request.app.state.db.update_one('users', {"_id" : create_objectid("Dummy")}, user_data, True)
    return {"data" : success}

@router.post("/change-password")
async def change_password(request: Request):
    form_data = await request.form()
    email = form_data.get("EMAIL")
    password = form_data.get("PASSWORD")
    success = request.app.state.db.update_one('users', {"EMAIL" : email}, {
      'PASSWORD' : password
    })
    return {"data" : success}