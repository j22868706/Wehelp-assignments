### Assignment - Week 5
---
#### 要求三: SQL CRUD  
- 3-1  
  - SQL command:  
    
    INSERT INTO member (name, username, password, follower_count) VALUES ('Jerry', 'test', 'test', '100');  

    ![新增資料](AssignmentImg/1.png)

- 3-2
  - SQL command:  
    SELECT * FROM member;
  ![新增資料](AssignmentImg/2.png)
    
- 3-3
  - SQL command:  
    SELECT * FROM member ORDER BY time DESC;
  ![新增資料](AssignmentImg/3.png)

- 3-4
  - SQL command:  
    SELECT * FROM member ORDER BY time DESC limit 1,3;
  ![新增資料](AssignmentImg/4.png)

- 3-5
  - SQL command:  
    SELECT * FROM member WHERE username = 'test';
  ![新增資料](AssignmentImg/5.png)

- 3-6
  - SQL command:  
    SELECT * FROM member WHERE username = 'test' AND password = 'test';
  ![新增資料](AssignmentImg/6.png)

- 3-7
  - SQL command:  
    UPDATE member SET name = 'test2' WHERE username = 'test';
  ![新增資料](AssignmentImg/7.png)

#### 要求四: SQL Aggregate Function
- 4-1
  - SQL command:  
  SELECT COUNT(id) FROM member;
  ![新增資料](AssignmentImg/8.png)

- 4-2
  - SQL command:  
  SELECT SUM(follower_count) FROM member;
  ![新增資料](AssignmentImg/9.png)

- 4-3
  - SQL command:  
  SELECT AVG(follower_count) FROM member;
  ![新增資料](AssignmentImg/10.png)