from pydnatic import BaseModel

class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    completed: bool