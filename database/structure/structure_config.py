SONG_TABLE = "song"
SONG_TABLE_PK = "song_id"
SONG_EXISTS_QUERY = {
    "query" : "SELECT * FROM song WHERE itunes_song_id=%s",
    "keys"  : ["itunes_song_id"]
}

SONG_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE s, sa, sav " + \
        "FROM song s " + \
        "INNER JOIN artist_song AS sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE s.song_id=sa.song_id " + \
        "AND sa.artist_song_id=sav.artist_song_id " + \
        "AND s.song_id=%s",
    "keys"  : ["song_id"]
}

ARTIST_TABLE = "artist"
ARTIST_TABLE_PK = "artist_id"
ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist WHERE itunes_artist_id=%s",
    "keys"  : ["itunes_artist_id"]
}
ARTIST_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE a, sa, sav " + \
        "FROM artist a " + \
        "INNER JOIN artist_song AS sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE a.artist_id=sa.artist_id " + \
        "AND sa.artist_song_id=sav.artist_song_id " + \
        "AND a.artist_id=%s ",
    "keys"  : ["artist_id"]
}

ARTIST_SONG_TABLE = "artist_song"
ARTIST_SONG_TABLE_PK = "artist_song_id"
ARTIST_SONG_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist_song WHERE artist_id=%s AND song_id=%s",
    "keys"  : ["artist_id", "song_id"]
}
ARTIST_SONG_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE sa, sav " + \
        "FROM artist_song sa " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE sa.artist_song_id=sav.artist_song_id " + \
        "AND sa.artist_song_id=%s ",
    "keys"  : ["artist_song_id"]
}

ARTIST_SONG_VIDEO_TABLE = "artist_song_video"
ARTIST_SONG_VIDEO_TABLE_PK = "artist_song_video_id"
ARTIST_SONG_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM artist_song_video WHERE artist_song_id=%s AND video_id=%s",
    "keys"  : ["artist_song_id", "video_id"]
}

YOUTUBE_VIDEO_TABLE = "youtube_video"
YOUTUBE_VIDEO_TABLE_PK = "video_id"
YOUTUBE_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM youtube_video WHERE youtube_video_id=%s",
    "keys"  : ["youtube_video_id"]
}
YOUTUBE_VIDEO_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE v, sav " + \
        "FROM youtube_video v " + \
        "INNER JOIN artist_song_video AS sav " + \
        "WHERE v.video_id=sav.video_id AND v.video_id=%s",
    "keys"  : ["video_id"]
}

USER_TABLE = "user"
USER_TABLE_PK = "user_id"
USER_EXISTS_QUERY = {
    "query" : "SELECT * FROM user WHERE email=%s",
    "keys"  : ["email"]
}

USER_REMOVE_ALL_REFERENCES_QUERY = {
    "query" : \
        "DELETE u, uh " + \
        "FROM user u " + \
        "INNER JOIN user_search_history AS uh " + \
        "WHERE u.user_id=uh.user_id AND u.user_id=%s",
    "keys"  : ["user_id"]
}

USER_SEARCH_HISTORY_TABLE = "user_search_history"
USER_SEARCH_HISTORY_TABLE_PK = "history_id"
USER_SEARCH_HISTORY_EXISTS_QUERY = {
    "query" : "SELECT * FROM user_search_history WHERE history_id=%s",
    "keys"  : ["history_id"]
}

JOIN_SONG_VIDEO_ARTIST_VIEW = "join_song_video_artist"
JOIN_SONG_VIDEO_ARTIST_VIEW_PK = ["video_id", "artist_id", "song_id"]
JOIN_SONG_VIDEO_ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_video_artist WHERE youtube_video_id=%s " + \
              "AND itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["youtube_video_id", "itunes_artist_id", "itunes_song_id"]
}
JOIN_SONG_VIDEO_ARTIST_ENTITIES = [SONG_TABLE, ARTIST_TABLE, ARTIST_SONG_TABLE,
                             ARTIST_SONG_VIDEO_TABLE, YOUTUBE_VIDEO_TABLE]

JOIN_SONG_ARTIST_VIEW = "join_song_artist"
JOIN_SONG_ARTIST_VIEW_PK = ["artist_id", "song_id"]
JOIN_SONG_ARTIST_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_artist WHERE itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["itunes_artist_id", "itunes_song_id"]
}
JOIN_SONG_ARTIST_ENTITIES = [SONG_TABLE, ARTIST_TABLE, ARTIST_SONG_TABLE]


JOIN_SONG_ARTIST_NO_VIDEO_VIEW = "join_song_artist_no_videos"
JOIN_SONG_ARTIST_NO_VIDEO_VIEW_PK = ["itunes_artist_id", "itunes_song_id"]
JOIN_SONG_ARTIST_NO_VIDEO_EXISTS_QUERY = {
    "query" : "SELECT * FROM join_song_artist_no_video WHERE itunes_artist_id=%s AND itunes_song_id=%s",
    "keys"  : ["itunes_artist_id", "itunes_song_id"]
}

JOIN_SONG_ARTIST_NO_VIDEO_ENTITIES = JOIN_SONG_ARTIST_ENTITIES

INSERT_QUERY = "INSERT INTO %s (%s) VALUES (%s)"
UPDATE_QUERY = "UPDATE %s SET %s WHERE %s=%s"
REMOVE_QUERY = "DELETE FROM %s WHERE %s=%s"
TRUNCATE_QUERY = "DELETE FROM %s"
SELECT_ALL_QUERY = "SELECT * FROM %s"
