#!/usr/bin/python3
"""contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer


Base = declarative_base()


class State(Base):
    """Inherits from base
    """
    __tablename__ = states
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                    .format("root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)