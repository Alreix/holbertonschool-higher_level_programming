-- Creates the database hbtn_0d_usa and the table cities with a foreign key to states

-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
