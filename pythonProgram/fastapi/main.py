from schema import TodoCreate, TodoUpdate
from fastapi import FastAPI, HTTPException
import models

app= FastAPI()

@app.get("/")
def todo():
    return {"message": "todo app running"}

@app.post("/todos")
def create_todo(todoCreate: TodoCreate):
    new_todo: list =models.create_todo(todo.title)
    return{"id": new_todo[0], "title": new_todo[1],
    "completed": new_todo[2], "created_at": new_todo[3]}

@app.get("/todos")
def get_all_todo():
    todos  = models.get_all_todo()
    result = []
    for todo in todos:
        result.append({"id": todo[0], "title": todo[1],
    "completed": todo[2], "created_at": todo[3]    }    )
    return {"message": "todo app running"}
