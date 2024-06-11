from sqlalchemy.orm import Session
from models import User, Discussion, Comment, Hashtag, DiscussionHashtag
from schemas import UserCreate, DiscussionCreate, CommentCreate
from auth import get_password_hash, verify_password
from fastapi import HTTPException, status

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(name=user.name, mobile_no=user.mobile_no, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user

def create_discussion(db: Session, discussion: DiscussionCreate, user_id: int):
    db_discussion = Discussion(text=discussion.text, image=discussion.image, user_id=user_id)
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    
    for tag in discussion.hashtags:
        db_tag = db.query(Hashtag).filter(Hashtag.tag == tag).first()
        if not db_tag:
            db_tag = Hashtag(tag=tag)
            db.add(db_tag)
            db.commit()
            db.refresh(db_tag)
        db_discussion_hashtag = DiscussionHashtag(discussion_id=db_discussion.id, hashtag_id=db_tag.id)
        db.add(db_discussion_hashtag)
        db.commit()
    
    return db_discussion
