-- lists all genres of the show Dexter.
SELECT tg.name AS name
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON tsg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
