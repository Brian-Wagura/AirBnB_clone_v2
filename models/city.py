#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """The city class, contains state ID and name
    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__(str): The name of the MySQL table to store Cities.
        state_id(sqlalchemy String): The state id of the city.
        name(sqlalchemy String): The name of the city
    """

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
