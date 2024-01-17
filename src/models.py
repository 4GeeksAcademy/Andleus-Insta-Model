import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'USERS'
    users_id = Column(Integer, primary_key=True)
    users_username = Column(String, primary_key=True)
    users_name = Column(String(250), nullable=False)
    
    users_followers = relationship('Follower', back_populates='follower_who')
    

class Post(Base):
    __tablename__ = 'POSTS'
    posts_id = Column(Integer, primary_key=True)
    posts_user_id = Column(String, ForeignKey('USERS.user_id'), nullable=False)
    posts_image = Column(String(250), nullable=False)
    posts_description = Column(String(500), nullable=False)
    
    posts_comments = relationship('Comment', back_populates='comment_from_post')
    

class Comment(Base):
    __tablename__ = 'COMMENTS'
    comments_id = Column(Integer, primary_key=True)
    comments_user_id = Column(String, ForeignKey('USERS.user_id'), nullable=False)
    comments_post = Column(Integer, ForeignKey('POSTS.post_id'), nullable=False)
    comments_content = Column(String(500), nullable=False)
    comments_date = Column(Date, nullable=False)
    
    comments_from_post = relationship('Post', back_populates='post_comments')
    


class Follower(Base):
    __tablename__ = 'FOLLOWERS'
    followers_id = Column(Integer, primary_key=True, autoincrement=True)
    followers_user = Column(Integer, ForeignKey('USERS.user_id'))
    followers_follower = Column(Integer, ForeignKey('USERS.user_id'))
    followers_date_start = Column(Date)

    followers_who = relationship('User', back_populates='user_followers')



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
