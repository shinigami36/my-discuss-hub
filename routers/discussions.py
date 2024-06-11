from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import Discussion, DiscussionCreate
from crud import create_discussion
from auth import oauth2_scheme

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/discussions/", response_model=Discussion)
def create_new_discussion(discussion: DiscussionCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_current_user(db, token)
    return create_discussion(db=db, discussion=discussion, user_id=user.id)
