from pydantic import BaseModel


class CreateTask(BaseModel):
    name: str
    due_date: str
    lead_time: str
    # check_mark: bool
    # category: int

class UpdateTask(BaseModel):
    name: str
    due_date: str
    lead_time: str
    # check_mark: bool

class CreateSubtask(BaseModel):
    name: str
    due_date: str
    lead_time: str
    # check_mark: bool
    task_id: int

class UpdateSubtask(BaseModel):
    name: str
    due_date: str
    lead_time: str
    # check_mark: bool

# class CreateCategory(BaseModel):
#     name: str
#     parent_id: int



