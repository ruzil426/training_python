from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
users = []
class User(BaseModel):
    user_id: int
    username: str
    age: int
@app.get("/users")
async def get_all_users() -> List[User]:
    return users
@app.post("/user/{username}/{age}")
async def create_user(username: User, age: User):
    if not users:
        user_id = 1
    else:
        user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'
@app.put("/user/{user_id}/{user_name}/{age}")
async def update_user(user_id: User, username: User, age: User):
    try:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f'User {user_id} has been updated'
    except IndexError:
        raise HTTPException(status_code=404, detail="User_id not found")
@app.delete("/user/{user_id}")
async def delete_user(user_id):
    try:
        users.pop(user_id)
        return f'User {user_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="User_id not found")
