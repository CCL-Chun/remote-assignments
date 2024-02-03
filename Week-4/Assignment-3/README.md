# Practice steps

## Run the HTTP server by running run.py directly
```
python run.py
```
## Setup MySQL server and database schema:
* Create a database named assignment
```
CREATE DATABASE assignment;
USE assignment;
```
* Create a user table named user with 4 columns
```
CREATE TABLE user (id VARCHAR(20), email NVARCHAR(255), name VARCHAR(20), age TINYINT);
ALTER TABLE user CHANGE name password VARCHAR(30);
```
* Password column needs more length to store after hashing by flask_bcrypt
```
ALTER TABLE user CHANGE password password VARCHAR(255) ;
```
* Set column id as the AUTO_INCREMENT primary key (increase automatically) and add the name column
```
ALTER TABLE user CHANGE id id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE user ADD COLUMN user VARCHAR(255);
SHOW COLUMNS FROM user; #check columns in the user table#
```

## Build a simple HTTP server using Flask

## Connect to MySQL using pymysql
* 