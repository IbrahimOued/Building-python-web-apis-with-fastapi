from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional

class TodoItem(BaseModel):
    item: str
    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class Todo(BaseModel):
    id: Optional[int]
    item: str
    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)
    class Config:
        Schema_extra = {
            "Example": {
                "id": 1,
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]
    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }