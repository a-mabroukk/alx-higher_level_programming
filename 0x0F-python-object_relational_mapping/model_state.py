#!/usr/bin/python3
import MySQLAlchemy
from MySQLAlchemy import Column, Integer, PrimaryKey, String, CHAR
from MySQLAlchemy.exit.declarative import declarative_base()

Base = declarative_base():
    class State(Base):
        """class definition"""
        __tablename__ = "state"
        name = Column(String(128))
        id = Column(Integer, primary_key=True)
