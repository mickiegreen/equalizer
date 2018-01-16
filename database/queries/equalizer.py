EQUALIZER = {
    'query' :   'SELECT %.2f*views + %.2f*comments + %.2f*likes + %.2f*dislikes AS score, youtube_video_title, youtube_video_id '
                'FROM join_song_video_artist '
                'WHERE genre = "%s" '
                'AND country = "%s" '
                'ORDER BY score '
                'LIMIT 10',
    'mode'  : 'select',
    'args': ['views','comments', 'likes', 'dislikes', 'genre', 'country']
}


SELECT_GENRE = {
    'query':
        'SELECT distinct(genre) as genre '
        'from song ',
    'mode' : 'select'
}


SELECT_COUNTRY = {
    'query':
        'SELECT distinct(country) as country '
        'from song ',
    'mode' : 'select'
}