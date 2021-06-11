-- Write a SQL script that creates a table users
-- TABLE users
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255)
)