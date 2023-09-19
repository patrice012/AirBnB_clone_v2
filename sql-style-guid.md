# SQL workflow
## Migration to MySQL database

## Development DataBase (hbnb_dev_db)

For root user --> Use `Root user password`
For hbnb_dev --> Use `hbnb_dev_pwd` as password

```
cat setup_mysql_dev.sql | sudo mysql -hlocalhost -uroot -p
echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | sudo mysql -uroot -p
```


## Test DataBase (hbnb_test_db)

For root user --> Use `Root user password`
For hbnb_test --> Use `hbnb_test_pwd` as password

```
cat setup_mysql_test.sql | sudo mysql -hlocalhost -uroot -p
echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | sudo mysql -uroot -p
```

## Helpers
```
SHOW DATABASES;
SHOW TABLES;
USE  database_name;
DROP DATABASEs IF EXISTS `hbnb_dev_db`;
DELETE FROM `TABLE_NAME` WHERE `condition`;
```

## 6. DBStorage - States and Cities 
create state
```
echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```
get State id and save it eg: `state_id = c6ff0f0b-2646-46b8-8a84-50051f8e3844`

View State information
`echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db`

City creation (replace state_id with your state id saved earlier in state_id)
```
echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

View Cities Information
`echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db`

## 7. DBStorage - User
Create User in db.
```
echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
```

View Users
`echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db`


## 8. DBStorage - Place 
Create place
Note: city_id is the ID of city in your database. Samething for User 
```echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

View City information
```echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db```