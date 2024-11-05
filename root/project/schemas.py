from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TeamMemberBase(BaseModel):
    id: int
    name: str
    role: str

class ProjectBase(BaseModel):
    project_id: int
    name: str
    start_date: date
    end_date: date
    team_members: List[TeamMemberBase]

class UserBase(BaseModel):
    name: str
    email: str
    contact_phone: str
    projects: List[ProjectBase]

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
