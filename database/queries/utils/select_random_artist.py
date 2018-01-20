"""
get random artist query
"""

SELECT_RANDOM_ARTIST = {
    'query':
        """
        SELECT artist_id, artist_name
        FROM(
            SELECT artist_id, artist_name
            FROM artist
            ORDER BY RAND()
        ) AS rand_artist
        LIMIT 1 
        """,
    'mode' : 'select'
}