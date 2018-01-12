POPULAR_GENRE_SONGS = {
    'query' :  'SELECT youtube_video_id, youtube_video_title '
                'FROM(SELECT youtube_video_id, youtube_video_title,sum(0.3*views+0.5*likes+0.2*comments) AS rating '
                'FROM join_song_video_artist '
                'where genre=( '
                'Select genre '
                'From( '
                'Select genre , sum(views) '
                'From join_song_video_artist '
                'group by genre '
                'Order by  sum(views) ASC '
                'Limit 1 ) as genre_table) '
                'group by video_id '
                'Order by  rating ASC '
                'limit  1) as  loved_song ',

    'mode': 'select'

}