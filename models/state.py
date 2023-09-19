#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    # if storage_type == "db":
    #     cities = relationship(
    #         "City", backref="state", cascade="all, delete, delete-orphan"
    #     )

    # else:
        # in order to match the test test_name3 for test_state classs
        # name = ""
    if storage_type != 'db':
        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
            """
            from models import storage

            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
