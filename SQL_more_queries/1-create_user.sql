-- Creates MySQL user user_0d_1@localhost with full privileges and a password

-- Create user_0d_1 if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply privilege changes
FLUSH PRIVILEGES;
