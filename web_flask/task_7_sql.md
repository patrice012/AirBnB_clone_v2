### log into python console
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
```

Test the current db
```
>>> from models import storage
>>> from models.state import State
>>> len(storage.all(State))
5
>>> len(storage.all(State))
5
>>> # Time to insert new data!
```

in other tabs insert new record into `states db`

```
echo 'INSERT INTO `states` (id, created_at, updated_at, name) VALUES ("421a55f1-7d82-45d9-b54c-a76916479545", NOW(), NOW(), "Alabama");' | sudo mysql -uroot -p hbnb_dev_db
```

Go back to python interpreter and test again
```
>>> # Time to insert new data!
>>> len(storage.all(State))
5
>>> # normal: the SQLAlchemy didn't reload his `Session`
>>> # to force it, you must remove the current session to create a new one:
>>> storage.close()
>>> len(storage.all(State))
6
>>> # perfect!
```

And for the getter cities in the State model: