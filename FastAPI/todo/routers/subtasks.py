from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from todo.backend.db_depends import get_db
from typing import Annotated
from todo.models.tasks import Task
from todo.models.subtasks import Subtask
from todo.schemas import CreateTask, UpdateTask, CreateSubtask, UpdateSubtask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/subtask", tags=["subtask"])

@router.get("/all_subtasks")
async def get_all_subtasks(db: Annotated[Session, Depends(get_db)]):
    get_all_subtasks = db.scalars(select(Subtask)).all()
    if len(get_all_subtasks) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Subtasks not found.')
    return get_all_subtasks
@router.post("/create_subtask")
async def create_subtask(db: Annotated[Session, Depends(get_db)], creating_subtask: CreateSubtask, task_id: int):
    db.execute(insert(Subtask).values(
                        name=creating_subtask.name,
                        due_date=creating_subtask.due_date,
                        lead_time=creating_subtask.lead_time,
                        # check_mark=creating_subtask.check_mark,
                        slug=slugify(creating_subtask.name),
                        task_id=task_id
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update_subtask")
async def update_task(db: Annotated[Session, Depends(get_db)], subtask_id: int, updating_subtask: UpdateSubtask):
    subtask = db.scalar(select(Subtask).where(Subtask.id == subtask_id))
    if subtask is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Subtask was not found.')
    db.execute(update(Subtask).where(Subtask.id == subtask_id).values(
        name=updating_subtask.name,
        due_date=updating_subtask.due_date,
        lead_time=updating_subtask.lead_time,
        # check_mark=updating_subtask.check_mark
        ))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Subtask update is successful!'}

@router.delete("/delete_subtask")
async def delete_subtask(db: Annotated[Session, Depends(get_db)], subtask_id: int):
    subtask = db.scalar(select(Subtask).where(Subtask.id == subtask_id))
    if subtask is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Subtask was not found.')
    db.execute(delete(Subtask).where(Subtask.id == subtask_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Subtask delete is successful!'}
