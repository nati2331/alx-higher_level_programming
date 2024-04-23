#!/usr/bin/python3
"""
Defines a model for representing cities, linking it to the states table.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city entity, inheriting from the Base class.

    Attributes:
        id: An auto-generated, unique integer primary key.
        name: A string column representing the city name (max length 128, not nullable).
        state_id: An integer column representing the foreign key to the states table (not nullable).
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
