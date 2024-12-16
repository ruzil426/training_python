from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from todo.backend.db_depends import get_db
from typing import Annotated
from todo.models.tasks import Task
from todo.models.subtasks import Subtask
from todo.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/all_tasks")
async def get_all_tasks(db: Annotated[Session, Depends(get_db)]):
    get_all_tasks = db.scalars(select(Task)).all()
    if len(get_all_tasks) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tasks not found.')
    return get_all_tasks
@router.post("/create_task")
async def create_task(db: Annotated[Session, Depends(get_db)], creating_task: CreateTask):
    db.execute(insert(Task).values(
                        name=creating_task.name,
                        due_date=creating_task.due_date,
                        lead_time=creating_task.lead_time,
                        check_mark=creating_task.check_mark,
                        slug=slugify(creating_task.name)
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update_task")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, updating_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found.')
    db.execute(update(Task).where(Task.id == task_id).values(
        name=updating_task.name,
        due_date=updating_task.due_date,
        lead_time=updating_task.lead_time,
        check_mark=updating_task.check_mark))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete("/delete_task")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found.')
    db.execute(delete(Task).where(Task.id == task_id))
    db.execute(delete(Subtask).where(Subtask.task_id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
