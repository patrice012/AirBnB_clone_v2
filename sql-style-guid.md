# SQL workflow

## Development DataBase (hbnb_dev_db)
`
For root user --> Use `Root user password`
For hbnb_dev --> Use `hbnb_dev_pwd` as password
`
```
cat setup_mysql_dev.sql | sudo mysql -hlocalhost -uroot -p
echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | sudo mysql -uroot -p
```


## Test DataBase (hbnb_test_db)
`
For root user --> Use `Root user password`
For hbnb_test --> Use `hbnb_test_pwd` as password
`
```
cat setup_mysql_test.sql | sudo mysql -hlocalhost -uroot -p
echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | sudo mysql -uroot -p
```

## Helpers
`
SHOW DATABASES;
SHOW TABLES;
USE  database_name;
DROP DATABASEs IF EXISTS `hbnb_dev_db`;
`