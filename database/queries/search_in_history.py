'''
A query to make the search through the history available.
This is the query we execute when we search in history on Equalizer.
'''
SEARCH_IN_HISTORY = {
     'query': '''
            SELECT youtube_video_id 
            FROM youtube_video,history_results,user_search_history 
            WHERE youtube_video.video_id=history_results.video_id and 
            history_results.history_id=user_search_history.history_id
            AND user_id="%d" and 
            MATCH (youtube_video_title) AGAINST ("%s" IN NATURAL LANGUAGE MODE)	
        ''',
        'mode': 'select',
        'args': ['user_id','search_string']
}

