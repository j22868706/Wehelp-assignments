### MySql: My study notes  
---

- Download and Install MySql server in MacBook m1  
  - .zsprofile: nono .zprofile
  - go to folder -> /usr ->  local -> bin -> press option -> Copy "bin" as Pathname  
  - type export PATH=${PATH}:paste the PATHNAME  
- to access MySql from terminal  
  - mysql -u root -p
---
##### SQL Statement
- CREATE DATABASE: is used to create a new SQL datebase
- USE DatabaseName: is used to select the database
- CREATE TABLE: is used to create a new table in database
  - Data types
    - BIGINT: a large integer.
    - INT: a medium integer.
      - UNSIGNED: defalut 0;
    - DATETIME: a date and time combination
      - CURRENT_TIMESTAMP
  - NOT NULL: to enforces a column to NOT accept NULL values
  - PRIMARY KEY:
      - Must contain UNIQUE values, and cannot contain NULL values
      - A table can have only ONE primary key
  - AUTO_INCREMENT
    - allows a unique number to be generated automatically when a new record is inserted into a table
- SHOW TABLE: is used to show the table in database
- DESC TableName: is used to retrieve infromation about a table's structure
  
