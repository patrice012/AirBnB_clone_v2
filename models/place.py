#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


from models.base_model import BaseModel, Base
from models import storage_type
from models.review import Review


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if storage_type == "db":
        reviews = relationship(
            "Review", cascade="all, delete, delete-orphan", backref="place"
        )

        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities",
        )

    if storage_type != "db":

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id equals to the\
            current Place.id => It will be the FileStorage relationship\
            between Place and Review
            """
            from models.__init__ import storage
            from models.amenity import Amenity

            related_places = []
            reviews = storage.all(Review)
            for obj in reviews.values():
                if obj.place_id == self.id:
                    related_places.append(obj)
            return related_places

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity\
            instances based on the attribute
            """
            from models.__init__ import storage
            from models.amenity import Amenity

            amenity_list = []
            amenities = storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for adding\
            an Amenity.id to the attribute amenity_ids
            """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
