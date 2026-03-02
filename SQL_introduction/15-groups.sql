-- Lists the number of records with the same score in second_table
-- Display score and count of records grouped by score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
