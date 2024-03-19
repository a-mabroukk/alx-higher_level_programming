#!/usr/bin/python3
"""python file that contains the class definition of a
State and an instance Base = declarative_base()"""
from MySQLAlchemy import Column, Integer, PrimaryKey, String
from MySQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class links to the `states` table of our database."""
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
