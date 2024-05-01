-- Creates a MySQL server with:
--  Database hbnb_dev_db
--  User hbnb_dev with password hbnb_dev_pwd in localhost
--  Grants all privileges to hbnb_dev on hbnb_dev_db
--  Grants SELECT privilege to hbnb_dev on performance_schema

DROP DATABASE IF EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES on `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;