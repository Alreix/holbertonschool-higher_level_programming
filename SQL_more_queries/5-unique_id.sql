-- Creates the table unique_id with a unique id column (default: 1)

-- Create table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INTEGER DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
