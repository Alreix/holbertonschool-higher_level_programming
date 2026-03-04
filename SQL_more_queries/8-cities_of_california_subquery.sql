-- Lists all cities of California from the database hbtn_0d_usa

-- Select cities where state_id matches the id of the state named California
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = "California"
)
ORDER BY id ASC;
