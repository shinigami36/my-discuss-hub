from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import Comment, CommentCreate
from crud import create_comment
from auth import oauth2_scheme

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/comments/", response_model=Comment)
def create_new_comment(comment: CommentCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_current_user(db, token)
    return create_comment(db=db, comment=comment, user_id=user.id)
