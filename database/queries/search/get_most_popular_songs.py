"""
This is a query which selects top 10 most popular music videos.
Each music video get a score. The score is calculated as followed:
score = video_views + 2.5*video_comments + video_likes + video_dislikes.
We decided a popular song is a song who has a lot of comments, likes, dislikes, views and favorited a lot.
The most important parameters for us was comments and favorites.
In the score the comments has a 2.5 weight factor to all other parameters.
Because some uploaders can turn off comments to a video, we also select the 5 music videos with the most views.
After we get 15 music videos (10 with highest score + 5 with most views) we select the top 10 favored music videos. 
Meaning out of 15 music videos, final 10 music videos are the ones who people favorite the most.
"""

MOST_POPULAR_SONGS = {
    'query' :'''
            SELECT youtube_video_title, youtube_video_id, video_id
            FROM (
                SELECT *
                FROM (
                    SELECT video_id, youtube_video_title, youtube_video_id, favorites,
                        views + 2.5 * comments + likes + dislikes AS score
                    FROM artist_song_video_view AS A
                    GROUP BY video_id
                    ORDER BY score DESC
                    LIMIT 5
                ) AS C
                UNION (
                    SELECT video_id, youtube_video_title, youtube_video_id, favorites, 
                        0 AS score
                    FROM artist_song_video_view AS B
                    WHERE comments=0
                    ORDER BY views DESC
                    LIMIT 5
                )
                ORDER BY favorites, score
            ) AS most_list_popular
            ''',
    'mode'  : 'select',
}
