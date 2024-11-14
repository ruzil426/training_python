from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    get_all_tasks = db.scalars(select(Task)).all()
    if len(get_all_tasks) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tasks not found.')
    return get_all_tasks

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found.')
    return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], task4user: CreateTask, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found.')
    db.execute(insert(Task).values(
        title=task4user.title,
        content=task4user.content,
        priority=task4user.priority,
        slug=slugify(task4user.title.lower()),
        user_id=user_id
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, updating_task: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found.')
    db.execute(update(Task).where(Task.id == task_id).values(
        title=updating_task.title,
        content=updating_task.content,
        priority=updating_task.priority,
        slug=slugify(updating_task.title)
    ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task was not found.')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}

