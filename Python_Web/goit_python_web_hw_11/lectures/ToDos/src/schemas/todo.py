from typing import Optional
from pydantic import BaseModel, Field

class TodoSchema(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=3, max_length=250)
    completed: Optional[bool] = False

class TodoUpdateSchema(TodoSchema):
    completed: bool

class TodoResponceSchema(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True