-- lists all records of the table second_table where name != null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
