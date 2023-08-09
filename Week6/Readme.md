#### 0808
---
- Create Connection 
  - command:   
    ```py
    import mysql.connector
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword") 
  
  - How to fix mysql.connector.errors NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported
    - uninstall mysql-connector and mysql-connector-python
    - re-install mysql-connector-python
 
  