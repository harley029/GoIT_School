from pydantic import BaseModel, Field, EmailStr
from datetime import date


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    birthday: date
    additional_data: str = Field(max_length=250, nullable=True)


class ContactUpdateSchema(ContactSchema):
    first_name: str
    last_name: str
    email: EmailStr
    birthday: date
    additional_data: str


class ContactResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    birthday: date
    additional_data: str

    class Config:
        orm_mode = True
