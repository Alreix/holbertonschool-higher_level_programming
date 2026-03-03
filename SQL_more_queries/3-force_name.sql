-- Creates the table force_name with a non-null name column

-- Create table force_name if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INTEGER,
    name VARCHAR(256) NOT NULL
);
