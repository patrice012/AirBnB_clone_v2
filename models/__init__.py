#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

# HBNB_ENV: running environment.\
# It can be “dev” or “test” for the moment (“production” soon!)
# HBNB_MYSQL_USER: the username of your MySQL
# HBNB_MYSQL_PWD: the password of your MySQL
# HBNB_MYSQL_HOST: the hostname of your MySQL
# HBNB_MYSQL_DB: the database name of your MySQL
# HBNB_TYPE_STORAGE: the type of storage used.\
# It can be “file” (using FileStorage) or db (using DBStorage)

storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
storage.reload()
