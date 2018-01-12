EQUALIZER = {
    'query' :   'SELECT 0.1*views + 0.2*comments + 0.3*likes + 0.2*genre + 0.2*country AS score, youtube_video_title, youtube_video_id '
                'FROM join_song_vide_artist '
                'WHERE genre = "%s" '
                'AND country = "%s" '
                'ORDER BY score '
                'LIMIT 10',
    'args'  : ['genre', 'country'],
    'mode'  : 'select'
}