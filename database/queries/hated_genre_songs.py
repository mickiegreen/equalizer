HATED_GENRE_SONGS = {
    'query' :   'SELECT youtube_video_id, youtube_video_title '
                'FROM(SELECT youtube_video_id, youtube_video_title,sum(0.3*views+0.5*likes+0.2*comments) AS rating'
                'FROM join_song_video_artist'
                'where   genre=('
                'Select genre'
                'From('
                'Select song.genre as genre , sum(youtube_video .views)'
                'From join_song_video_artist'
                'group by song.genre'
                'Order by  sum(youtube_video .views)'
                'Limit 1 ) as genre_table)'
                'group by video_id'
                'Order by  rating '
                'limit  1) as  worst_song',

    'mode': ['select']

}