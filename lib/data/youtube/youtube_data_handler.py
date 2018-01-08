# -*- coding: utf-8 -*-

# Copyright (c) 2018 Michael Green
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
import time
import re

from overrides import overrides

from .. import AbstractDataHandler
from equalizer.lib.storage.mysql.entities import ArtistSong, \
    ArtistSongVideo, YoutubeVideo, JoinSongVideoArtist, \
    JoinSongArtistNoVideo

from equalizer.lib.api import youtube
from equalizer.lib.utils import generate_random_str

import logging

logger = logging.getLogger()

class YoutubeDataHandler(AbstractDataHandler):
    """ youtube data adapter to update existing storage """

    def __init__(self, engine, token, youtube_keys = {}, search_keys = [], chars_to_remove = '[]'):
        """
        :param engine: storage engine
        :param youtube_keys: keys that youtube data object must contain
        """
        super(YoutubeDataHandler, self).__init__(engine)

        if not isinstance(youtube_keys, dict):
            raise TypeError("keys must be dict")

        self._keys = youtube_keys
        self._token = token
        self._search_keys = search_keys
        self._chars_to_remove = '[' + ''.join(chars_to_remove) + ']'

        # adding token to youtube api adapter
        youtube.add_token(token)

    def add(self, data):
        """
        adding youtube data to storage
        :param data - data of youtube:
        """

        if not self.validate(data):
            raise Exception("youtube data isn't valid. Make sure "
                            "it's not missing important data, and "
                            "isn't duplicated")

        _json = data.dict()

        # creating new video entity and adding it
        youtube_video = YoutubeVideo(**_json)
        video_id = self.engine.update_if_exists_else_add(youtube_video)

        # handling error
        if video_id == -1:
            raise RuntimeError("video wasn't added to db :: " + str(_json))

        _json.update(youtube_video.dict())

        # getting primary key of (song_id, artist_id)
        _json.update(**{'artist_song_id' : self.engine.get(ArtistSong(**_json))})

        # handling error - assuming artist_song exists in db
        if _json['artist_song_id'] == -1:
            raise RuntimeError("couldn't get artist_song_id of "
                               "song_id=%d and artist_id=%d :: " %(_json['song_id'], _json['artist_id']))

        # creating new artist_song_video_entry and add it to db
        artist_song_video = ArtistSongVideo(**_json)
        artist_song_video_id = self.engine.update_if_exists_else_add(artist_song_video)

        # handle error if couldn't update database
        if artist_song_video_id == -1:
            raise RuntimeError("artist_song_video with "
                               "artist_song_id=%d & video_id=%d wasn't added to db" %(video_id, _json['artist_song_id']))

        # updating original object
        data.update(**_json)

    @overrides
    def add_from_local_folder(self, folder, limit=20000, update=True):
        """
        add entries from file system
        first check they don't already exist in db
        :param folder - directory to fetch files from:
        """

        # load results
        youtube_data = self._load_youtube_entries(folder, limit)

        for entry in youtube_data:
            # if data exists - just update
            if self.exists(entry) and update:
                self.update(entry)

            # else add it
            else:
                self.add_if_valid(entry)

    def update(self, data):
        """ update existing data """

        if not isinstance(data, YoutubeVideo):
            raise TypeError("data must be of type YoutubeVideo")

        if not self.engine.exists(data):
            raise ValueError("update must be executed on existing entries")

        # retrieve up-to-date data from youtube
        data.update(**self._get_video(data['youtube_video_id']))

        # updating database with new data
        self.engine.update(data)

        # return updated data
        return data

    def update_all(self):
        """ update all entries in db """

        # get all rows from table
        data = self.engine.fetch_all_like_entry(YoutubeVideo())

        # update each
        for row in data: self.update(row)

    def complete_storage_data(self, song_data, update = True, limit = 3):
        """
        complete data from songs and artists that misses youtube video
        :param limit - max entries for search
        """

        if not isinstance(song_data, JoinSongArtistNoVideo):
            raise TypeError("data must be of type JoinSongArtistNoVideo")

        # getting videos according to data
        videos = self._get_videos(song_data, limit=limit)

        for video in videos:

            # if video exists just update if flag
            if self.exists(video) and update:

                # getting original object
                self.engine.get(video)

                # updating video after data is fetched
                video.update(**self.update(YoutubeVideo(**video.dict())).dict())

            # else add if contains all required data
            elif not self.exists(video):

                # getting video statistics and info from youtube
                video.update(**self._get_video(video['youtube_video_id']))

                # adding if all required data has been fetched
                self.add_if_valid(video)

        return [video.json() for video in videos]

    def complete_all_storage_data(self, output_dir, limit = 3,
                                  itunes_keys = {}, update = True,
                                  chunk_size = 100):
        """
        complete data from itunes that misses youtube video
        :param limit - max entries for search
        :param chunk_size - number of entries to save in one file of youtube
        """

        # getting itunes data from table where no youtube data found
        data = self.engine.fetch_all_like_entry(JoinSongArtistNoVideo())[:200]

        results = []

        # for each entry in data with no video - get more videos and add if not exist
        for row in data:
            row_data = row.copy()

            # convert itunes data to youtube
            self._parse_itunes(row_data, itunes_keys = itunes_keys)

            # searching results and updating database
            results.extend(self.complete_storage_data(row_data, limit = limit, update = update))

            # writing to file if chuck size has reached
            if len(results) >= chunk_size:
                self._write_results_to_file(output_dir, results)

                results = []

        # write final results to output file
        self._write_results_to_file(output_dir, results)

    def get(self, data):
        """ get existing data from storage """
        raise NotImplementedError

    def get_all(self):
        """ return all data from storage """
        raise NotImplementedError

    def exists(self, data):
        """ return True if data exists in storage else False """

        # force data object type
        if not isinstance(data, JoinSongVideoArtist) :
             raise TypeError("data must be of type JoinSongVideoArtist")

        # check if exists
        return self.engine.get(data) != -1

    def remove(self, data):
        """ remove data from storage """
        raise NotImplementedError

    def remove_all(self):
        """ clear all data """
        raise NotImplementedError

    def uptodate(self, data):
        """ return True if data is up-to-date else False """
        raise NotImplementedError

    def get_more_data(self, params = {}, limit = 2000):
        """
        add new entries to database
        @limit - max num of records to add
        @params - search query
        """
        raise NotImplementedError

    def validate(self, data):
        """
        :param data: validate
        :return: True if data contains all keys
        """

        if not isinstance(data, JoinSongVideoArtist) :
            raise TypeError("data must be of type JoinSongVideoArtist")

        keys = self._keys.values()

        # if data doesn't have all required keys return False
        for k in keys:
            if not hasattr(data, k['key']) or data[k['key']] == None:
                return False

        return True

    def _load_youtube_entries(self, folder, limit = 20000):
        """ fetch all youtube data from local folder """
        youtube = []

        for dirName, subdirList, fileList in os.walk(folder):

            for _file in fileList:
                if not _file.endswith(".txt"): continue

                with open(folder + os.sep + _file, 'r') as _f:

                    # merge all results to one list
                    youtube.extend(map(lambda x : JoinSongVideoArtist(**x), json.load(_f)))

                if len(youtube) >= limit:
                    break

        return youtube

    def _search_keywords(self, song_data):
        """
        return keywords of entry - artist_name, track_title
        :param data:
        :return:
        """
        # fetch keywords from song_data
        keywords = []
        _json = song_data.dict()

        for key in self._search_keys:
            value = re.sub(self._chars_to_remove, '', _json.get(key, ''))
            keywords.extend(value.split(' '))

        return keywords

    def _get_videos(self, song_data, limit = 3):
        """
        getting data from youtube according to itunes_data
        :param itunes_data: itunes record to search
        """

        # get song keywords
        keywords = self._search_keywords(song_data)

        # search for videos with same keywords
        videos = youtube.search(keywords, keys = self._keys.keys())[:limit]

        new_song_videos = []

        for video in videos:
            # video to mysql structure
            video_info = {
                self._keys[k]['key']: self._parse(self._keys[k], k, video)
                for k, v in video.iteritems() if self._keys.__contains__(k)
            }

            # add song data to entry
            video_info.update(**song_data.dict())
            video_info = JoinSongVideoArtist(**video_info)

            # add video
            new_song_videos.append(video_info)

        return new_song_videos

    def _get_video(self, youtube_video_id):
        """ fetching single video data & statistics """

        more_info = youtube.get(youtube_video_id, keys=self._keys.keys())

        # convert to mysql format
        more_info_to_mysql = {
            self._keys[k]['key']: self._parse(self._keys[k], k, more_info)
            for k, v in more_info.iteritems() if self._keys.__contains__(k)
        }

        return more_info_to_mysql

    def _parse(self, v, k, entry):
        """ parse k according to v parser """
        return v['parser']().parse(entry[k])

    def _parse_itunes(self, data, itunes_keys = {}):
        """ fit itunes data to search in youtube """

        for k, v in itunes_keys.iteritems():
            if data[k] != None:
                data[k] = self._parse(v, k, data)

    def _write_results_to_file(self, output_dir, results):
        """ write results to file """

        with open(output_dir + os.sep + generate_random_str(20) + str(int(time.time())) + ".txt", 'w') as _file:
            json.dump(results, _file)

