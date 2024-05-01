-- Creates a MySQL server wih:
--  Database hbnb_test_db
--  User hbnb_test with password hbnb_test_pwd in localhost
--  User hbnb_test with all privileges on the database
--  Grants SELECT privilege on performance_schema to hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
   ON `hbnb_test_db`.*
   TO 'hbnb_test'@'localhost'
   IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT
    ON `performance_schema`.*
    TO 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;