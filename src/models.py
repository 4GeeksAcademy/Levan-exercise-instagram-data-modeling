import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))
    dob = Column(DateTime)
    last_login_time = Column(DateTime)

class Photo(Base):
    __tablename__ = 'photo'
    photo_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    photo_location = Column(String(250), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)

class Follow(Base):
    __tablename__ = 'follow'
    follow_id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.user_id'))
    user_id2 = Column(Integer, ForeignKey('user.user_id'))

class FeedItem(Base):
    __tablename__ = 'feed_item'
    feed_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    content = Column(String(250))
    photo_id = Column(Integer, ForeignKey('photo.photo_id'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    photo = relationship(Photo)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'preview.png')