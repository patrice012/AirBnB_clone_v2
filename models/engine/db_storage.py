#!/usr/bin/python3
"""
Module contains Class DBStorage use to manage\
database storage
"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class DBStorage:
    """
    This class manages storage of hbnb models to MySQL Server db
    Attributes:
        __engine (sqlalchemy.Engine) : the working SQLAlchemy engine
        __session (sqlalchemy.Session) : theworking SQLAlchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialises a new DBStorage instance"""
        dialect = "mysql"
        driver = "mysqldb"
        port = 3306
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        # create connection arg
        args = f"{dialect}+{driver}://{user}:{passwd}@{host}:{port}/{db_name}"
        # create connection
        self.__engine = create_engine(args, pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
            

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """
        add the object to the current database\
        session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current\
        database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        # create the current database session
        bind = self.__engine
        session_factory = sessionmaker(bind=bind, expire_on_commit=False)
        # to make sure the Session is thread-safe
        Session = scoped_session(session_factory)
        # set session
        self.__session = Session()
