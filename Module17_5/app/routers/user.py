from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user']) # !!!


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    get_all_users = db.scalars(select(User)).all()
    if len(get_all_users) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users not found.')
    return get_all_users

@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found.')
    return user

@router.get('/user_id/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found.')
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if len(tasks) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no tasks for the user.')
    return tasks

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], creating_user: CreateUser):
    user = db.scalar(select(User).where(User.slug == creating_user.username))
    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'The user with username {creating_user.username} already exists.')
    db.execute(insert(User).values(
                        username=creating_user.username,
                        firstname=creating_user.firstname,
                        lastname=creating_user.lastname,
                        age=creating_user.age,
                        slug=slugify(creating_user.username)
    ))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, updating_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found.')
    db.execute(update(User).where(User.id == user_id).values(
        firstname=updating_user.firstname,
        lastname=updating_user.lastname,
        age=updating_user.age))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found.')
    db.execute(delete(User).where(User.id == user_id))
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
