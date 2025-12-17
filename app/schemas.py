from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    group: str
    grade: float
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    group: str
    grade: float
    email: str

    class Config:
        from_attributes = True
