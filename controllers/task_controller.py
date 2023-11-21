


from models.task_model import Task

from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import List
# from models import Task



# Fake database to simulate data storage
tasks_db = []

# Controller
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


def get_tasks():
    if tasks_db or tasks_db == []:
        results = tasks_db[::]
        return results
    raise HTTPException(status_code=404, detail="Task not found")


def create_task(task: Task):
    task_dict = task.model_dump()
    task_dict["id"] = len(tasks_db) + 1
    tasks_db.append(task_dict)
    return task_dict

def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db[i] = updated_task.model_dump()
            tasks_db[i]["id"] = task_id
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Task not found")

def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            del tasks_db[i]
            return JSONResponse(content={"message": "Task deleted successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Task not found")
