-- Query to create the user 'user_0d_1' in MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
