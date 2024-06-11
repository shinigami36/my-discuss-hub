from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Text, Table
from sqlalchemy.orm import relationship
from database import Base
import datetime

# Many-to-many relationship table for following users
user_follow = Table(
    'user_follow', Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id')),
    Column('followed_id', Integer, ForeignKey('users.id'))
)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile_no = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    followers = relationship(
        "User",
        secondary=user_follow,
        primaryjoin=id==user_follow.c.follower_id,
        secondaryjoin=id==user_follow.c.followed_id
    )
    discussions = relationship("Discussion", back_populates="user")

class Discussion(Base):
    __tablename__ = 'discussions'
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    image = Column(String, nullable=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="discussions")
    hashtags = relationship("Hashtag", secondary="discussion_hashtag")
    comments = relationship("Comment", back_populates="discussion")

class Hashtag(Base):
    __tablename__ = 'hashtags'
    
    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, unique=True)

class DiscussionHashtag(Base):
    __tablename__ = 'discussion_hashtag'
    
    discussion_id = Column(Integer, ForeignKey('discussions.id'), primary_key=True)
    hashtag_id = Column(Integer, ForeignKey('hashtags.id'), primary_key=True)

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    discussion_id = Column(Integer, ForeignKey('discussions.id'))
    discussion = relationship("Discussion", back_populates="comments")
    likes = Column(Integer, default=0)
