#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import sqlalchemy
import models
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """The city class, contains state ID and name
    Inherits from SQLAlchemy Base and links to the MySQL table cities.
    """
    if models.storage_t == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        "initializes city"
        super().__init__(*args, **kwargs)

