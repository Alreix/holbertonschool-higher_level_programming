-- Lists all shows whitout a genre linked

-- Select show titles with their genre ids, ordered by title and genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- LEFT JOIN keeps all shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
-- Keep only shows whitout genre
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
