SELECT_RANDOM_GENRE = {
    'query':
        """
        SELECT genre 
        FROM (
            SELECT DISTINCT(genre) AS genre
            FROM song
            ORDER BY RAND()
        ) AS rand_genres 
        LIMIT 1
        """,
    'mode' : 'select'
}