-- Lists all genres and the number of shows linked to each genre

-- Select the genre name and count how many shows are linked to it
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
-- Group results by genre name to count shows per genre
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

