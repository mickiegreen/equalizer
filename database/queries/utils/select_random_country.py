SELECT_RANDOM_COUNTRY = {
    'query':
        """
        SELECT country
        FROM (
            SELECT DISTINCT(country) AS country
            FROM song
            ORDER BY RAND()
        ) AS countries
        LIMIT 1 
        """,
    'mode' : 'select'
}