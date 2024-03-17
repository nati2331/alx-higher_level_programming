#!/usr/bin/python3
"""
Defines the State model class, 
inheriting from Base, 
linking to the 'states' table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state entity, inheriting from the Base class.

    Attributes:
        id: An auto-generated, unique integer primary key.
        name: A string column representing the state name.
        cities: A relationship attribute representing 
        the cities associated with the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
