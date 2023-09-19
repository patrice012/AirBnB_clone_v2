#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


from models.base_model import BaseModel, Base
from models import storage_type
from models.review import Review
from models.amenity import Amenity


association_table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if storage_type != "db":

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id equals to the\
            current Place.id => It will be the FileStorage relationship\
            between Place and Review
            """
            from models.__init__ import  storage
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
            from models.__init__ import  storage
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
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)

