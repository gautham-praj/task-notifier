from pydantic import BaseModel, EmailStr

class Task(BaseModel):
    title: str
    description: str
    assignee_email: EmailStr
