-- Lists all records of second_table without rows missing a name
-- Display score and name ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
