'''
A query to make the search through the history available.
This is the query we execute when we search in history on Equalizer.
'''
FULLTEXT_SEARCH_IN_HISTORY = {
    'query':   'SELECT v.video_id, vft.youtube_video_id ' 
               'FROM youtube_video_fulltext vft, results_history r, youtube_video v ' 
               'WHERE v.youtube_video_id=vft.youtube_video_id '
               'AND v.video_id=r.video_id '
               'AND r.user_id=%d '
               'AND MATCH (vft.youtube_video_title) AGAINST ("%s" IN NATURAL LANGUAGE MODE)',
    'mode': 'select',
    'args': ['user_id','search_string']
}

