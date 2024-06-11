from pydantic import BaseModel, EmailStr
from typing import List, Optional
import datetime

class UserBase(BaseModel):
    name: str
    mobile_no: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class DiscussionBase(BaseModel):
    text: str
    image: Optional[str] = None

class DiscussionCreate(DiscussionBase):
    hashtags: List[str] = []

class Discussion(DiscussionBase):
    id: int
    created_on: datetime.datetime
    user_id: int
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_on: datetime.datetime
    user_id: int
    discussion_id: int
    likes: int
    class Config:
        orm_mode = True
