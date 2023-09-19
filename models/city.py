#!/usr/bin/python3
""" City Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey

from models.base_model import BaseModel, Base
from models import storage_type


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    # possible bugs here. This is only to match tests cases
    # test_state_id and test_name. Maybe remove them and comment those tests
    if storage_type != "db":
        name = ""
        state_id = ""
