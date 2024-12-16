from fastapi import FastAPI
from routers import tasks, subtasks
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='teplates')

@app.get("/")
async def greetings():
    return {'message': 'Список дел'}

app.include_router(tasks.router)
app.include_router(subtasks.router)



