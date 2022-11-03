-- lists all genres of the show Dexter.
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg
ON ts.id = tsg.show_id
INNER JOIN tv_genres AS tg
ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
