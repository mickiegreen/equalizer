import random
'''
This is a query which selects top 10 most popular music videos.
Each music video get a score. The score is calculated as followed:
score = video_views + 2.5*video_comments + video_likes + video_dislikes.
We decided a popular song is a song who has a lot of comments, likes, dislikes, views and favorited a lot.
The most important parameters for us was comments and favorites.
In the score the comments has a 2.5 weight factor to all other parameters.
Because some uploaders can turn off comments to a video, we also select the 5 music videos with the most views.
After we get 15 music videos (10 with highest score + 5 with most views) we select the top 10 favored music videos. 
Meaning out of 15 music videos, final 10 music videos are the ones who people favorite the most.
'''
MOST_POPULAR_SONGS = {
    'query' :  'SELECT youtube_video_id, youtube_video_title '
               'FROM '
               '(SELECT youtube_video_id, youtube_video_title '
               'FROM( '
               'SELECT youtube_video_title as title,youtube_video_id as id , '
               ' sum(0.3*views+0.5*likes+0.2*comments) AS rating '
               'FROM join_song_video_artist '
               'WHERE country IN(select country from song where YEAR(release_date) = "%s") ' 
               'GROUP BY id) rating_table '                
               'JOIN youtube_video  as main_table ON rating_table.id = main_table.youtube_video_id '
               'ORDER BY rating  desc'
               'limit 10) as a ',
    'args': ['release_date'],
    'mode'  : 'select',
    'default' : {"year":random.randint(1905,2018)}
}

HARELZ_MOST_POPULAR_SONGS = {
    'query' :  '''
    SELECT C.youtube_video_title, distinct C.youtube_video_id
    FROM
    (
        SELECT A.youtube_video_title, A.youtube_video_id, A.favorites,
                A.views + 2.5 * A.comments + A.likes + A.dislikes AS score
        FROM join_song_vide_artist AS A
        ORDER BY A.score
        LIMIT 10
        UNION (
        SELECT B.youtube_video_title, B.youtube_video_id, B.favorites,
                0 AS score
        FROM join_song_vide_artist AS B
        ORDER BY B.views
        LIMIT 5
        )
    ) AS C
    ORDER BY C.favorites, C.score
    LIMIT 10''',
    'args': ['release_date'],
    'mode'  : 'select',
    'default' : {"year":random.randint(1905,2018)}
}
