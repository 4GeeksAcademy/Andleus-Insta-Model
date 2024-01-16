import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'USERS'
    user_id = Column(Integer, primary_key=True)
    user_username = Column(String, primary_key=True)
    user_name = Column(String(250), nullable=False)
    
    user_followers = relationship('Follower', back_populates='follower_who')
    

class Post(Base):
    __tablename__ = 'POSTS'
    post_id = Column(Integer, primary_key=True)
    post_user_id = Column(String, ForeignKey('USERS.user_id'), nullable=False)
    post_image = Column(String(250), nullable=False)
    post_description = Column(String(500), nullable=False)
    
    post_comments = relationship('Comment', back_populates='comment_from_post')
    

class Comment(Base):
    __tablename__ = 'COMMENTS'
    commnent_id = Column(Integer, primary_key=True)
    comment_user_id = Column(String, ForeignKey('USERS.user_id'), nullable=False)
    comment_post = Column(Integer, ForeignKey('POSTS.post_id'), nullable=False)
    comment_content = Column(String(500), nullable=False)
    comment_date = Column(Date, nullable=False)
    
    comment_from_post = relationship('Post', back_populates='post_comments')
    


class Follower(Base):
    __tablename__ = 'FOLLOWERS'
    follower_id = Column(Integer, ForeignKey('USERS.user_id'), primary_key=True)
    follower_user = Column(Integer, ForeignKey('USERS.user_id'), primary_key=True)
    follower_date_start = Column(Date)

    follower_who = relationship('User', back_populates='user_followers')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
