import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user  '
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    last_name = Column(String(250), nullable=False)
    username = Column(String(80), nullable= False)
    email = Column( String(256), nullable= False , unique=True)



class Planets(Base): 

    __tablename__= "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String(180), nullable=False)
    atmosphere = Column(Boolean, nullable = False)

class Characters(Base):
    __tablename__ ='characters'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(300), nullable=False)
    hair_color =Column(String(30), nullable=True)
    eye_color = Column(String(30), nullable=True)


class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)

    User_id = Column(Integer,ForeignKey('user.id'), nullable=False)
    user=relationship(User)

    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    character = relationship(Characters)

    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    planet = relationship(Planets)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
