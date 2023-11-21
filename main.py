

from models.task_model import Task
from controllers.task_controller import get_task, create_task, delete_task , update_task , get_tasks


# main.py

from typing import List

from fastapi import FastAPI
app = FastAPI()

# View
@app.post("/tasks/", response_model=Task)
def create_task_route(task: Task):
    return create_task(task)

@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    return get_task(task_id)

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_route(task_id: int, updated_task: Task):
    return update_task(task_id, updated_task)

@app.delete("/tasks/{task_id}")
def delete_task_route(task_id: int):
    return delete_task(task_id)
