from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# Validation for input data when creating an owner
class OwnerSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr


# Validation for output data when reading from the database
class OwnerResponse(OwnerSchema):
    id: int=1

    class Config:
        from_attributes = True


class CatBase(BaseModel):
    nick: str = Field(default='Simon', min_length=3, max_length=25)
    age: int = Field(default=1, ge=1, le=30)
    vacinated: Optional[bool] = None

class CatSchema(CatBase):
    owner_id: int = Field(default=1, ge=1)

class CatResponse(CatBase):
    id: int = 1
    owner: OwnerResponse

    class Config:
        from_attributes = True
