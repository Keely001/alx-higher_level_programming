-- Query to create the user 'user_0d_1' in MySQL server
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

-- Reload privileges to apply the changes
FLUSH PRIVILEGES;
