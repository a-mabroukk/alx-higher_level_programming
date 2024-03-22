#!/usr/bin/python3
"""
module for database quering using SQLAlchemy
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session

from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
