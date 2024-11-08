from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int = 20


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)) -> HTMLResponse:
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(404, 'User was not found.')


@app.post("/user/{username}/{age}")
async def create_user(username:
                Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='35')]):
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id = user_id, username = username, age = age)
    users.append(user)
    return f'User {user_id} is registered', user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='35')]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f'User {user_id} has been updated', user
    raise HTTPException(status_code=404, detail='User not found')

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f'User {user_id} has been deleted', user
    raise HTTPException(status_code=404, detail="User not found")