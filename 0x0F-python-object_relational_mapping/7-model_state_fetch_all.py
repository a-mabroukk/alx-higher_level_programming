#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://mysql+mysqldb'. @localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True, echo=True)

Base.metadata.create_all(bind=engine)

session = sessionmaker
session = session()

state = State()
for instance in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
