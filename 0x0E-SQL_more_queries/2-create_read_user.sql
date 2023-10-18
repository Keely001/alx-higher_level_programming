-- Creates the user 'user_0d_1' and the database 'hbtn_0d_2' in MySQL server

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';
SET PASSWORD FOR 'user_0d_2'@'%' = 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';
FLUSH PRIVILEGES;
