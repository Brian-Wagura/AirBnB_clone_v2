#!/usr/bin/python3
""" State Module for HBNB project """
import models
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv



class Amenity(BaseModel):
    """ Amenity class """
    if models.storage_t == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        "initializes amenity"
        super().__init__(*args, **kwargs)
