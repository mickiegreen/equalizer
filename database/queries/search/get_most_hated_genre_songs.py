'''
This is a query which selects top 10 most unliked music videos from a specific genre.
This query calculate rating for each music video based on it's views, likes and comments.
Then select the top 10 highest rated music videos, and filter it by it's genre.
The selected music videos will be of the most viewed music videos genre on youtube.
'''
MOST_HATED_GENRE_SONGS = {
    'query':'''
            SELECT  youtube_video_id, youtube_video_title, video_id
            FROM (
              SELECT youtube_video_id, youtube_video_title, video_id, sum(0.3*views+0.5*likes+0.2*comments) AS rating
              FROM artist_song_video_view
              WHERE genre IN (
                SELECT  genre
                FROM (
                  SELECT genre , SUM(views) AS viewsCount
                  FROM artist_song_video_view
                  GROUP BY genre
                  ORDER BY viewsCount
                  LIMIT 10
                ) as genre_table
            )
            GROUP BY  video_id
            ORDER BY  rating
            LIMIT  10) as  worst_song
            ''',
    'mode': 'select'
}