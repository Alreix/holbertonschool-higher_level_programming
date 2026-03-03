-- Creates the database hbtn_0d_usa and the table states

-- Create database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database hbtn_0d_usa
USE hbtn_0d_usa

-- Create table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id)
);
