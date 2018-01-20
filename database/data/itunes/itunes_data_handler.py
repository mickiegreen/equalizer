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
from overrides import overrides

from .. import AbstractDataHandler
from equalizer.database.structure import JoinSongArtistNoVideo, JoinSongArtist

class ItunesDataHandler(AbstractDataHandler):
    """ itunes data adapter to update existing storage """

    def __init__(self, engine, itunes_keys = {}, optional_keys = {},
                 additional_entries = []):
        """
        :param engine: storage engine
        :param itunes_keys: itunes api keys mapping to mysql keys and parser
        """
        super(ItunesDataHandler, self).__init__(engine)

        # force dict type on itunes_keys
        if not isinstance(itunes_keys, dict):
            raise TypeError("itunes_keys must be dict")

        # force dict type on optional_keys
        if not isinstance(optional_keys, dict):
            raise TypeError("optional_keys must be dict")

        # force list type on additional_entries
        if not isinstance(additional_entries, list):
            raise TypeError("additional_entries must be list")

        # force parsing structure on each key
        for k, v in itunes_keys.iteritems():
            if not isinstance(v, dict) or v.get('key', None) == None or v.get('parser', None) == None:
                raise ValueError("each key in itunes_keys must be of structure {<api_key> : {key : <mysql_key>, parser : <value_parser_object>} }")

        # force parsing structure on each key
        for k, v in optional_keys.iteritems():
            if not isinstance(v, dict) or v.get('key', None) == None or v.get('parser', None) == None:
                raise ValueError(
                    "each key in optional_keys must be of structure "
                    "{<api_key> : {key : <mysql_key>, parser : <value_parser_object>} }"
                )

        for entry_keys in additional_entries:
            if not isinstance(entry_keys, dict):
                raise TypeError("each entry_keys in additional_entries must be dict")

            # force parsing structure on each key
            for k,v in entry_keys.iteritems():
                if not isinstance(v, dict) or v.get('key', None) == None or v.get('parser', None) == None:
                    raise ValueError(
                        "each key in optional_keys must be of structure " + \
                        "{<api_key> : {key : <mysql_key>, parser : <value_parser_object>} }"
                    )

        self._keys = itunes_keys
        self._optional_keys = optional_keys
        self._additional_entries = additional_entries

    @overrides
    def add(self, data):
        """
        adding itunes data to storage
        :param data - one entry data of itunes:
        """

        if not self.validate(data):
            raise Exception("itunes data isn't valid. Make sure "
                            "it's not missing important data, and "
                            "isn't duplicated")

        return self.engine.add(JoinSongArtist(**data.dict()))

    @overrides
    def add_from_local_folder(self, folder, limit = 20000, update = True):
        """
        add entries from file system
        first check they don't already exist in db
        :param folder - directory to fetch files from:
        """

        # load results
        itunes_data = self._load_itunes_results(folder, limit)

        for entry in itunes_data:
            try:
                # if data exists - just update
                if self.exists(entry) and update: self.update(entry)

                # else add it
                else:
                    self.add_if_valid(entry)

            except Exception as e:
                print(e)

    @overrides
    def update(self, data):
        """ update existing data """

        if not isinstance(data, JoinSongArtist):
            raise TypeError("data must be of type JoinSongArtist")

        self.engine.update_if_exists_else_add(data)

    @overrides
    def update_all(self):
        """ update all entries in db """

        # get all rows from table
        data = self.engine.fetch_all_like_entry(JoinSongArtist())

        # update each
        for row in data: self.update(row)

    @overrides
    def get(self, data):
        """ get existing data from storage """

        # validating data structure
        if not self.validate(data) or not self.exists(data): return -1

        # updating data object and returning its id
        return self.engine.get(data)

    @overrides
    def get_all(self):
        """ return all data from storage """
        return self.engine.fetch_all_like_entry(JoinSongArtist())

    @overrides
    def exists(self, data):
        """ return True if data exists in storage else False """

        # force data object type
        if not isinstance(data, JoinSongArtistNoVideo) \
                and not isinstance(data, JoinSongArtist):
             raise TypeError("data must be of type JoinSongArtistNoVideo or JoinSongArtist")

        # check if exists
        return self.engine.get(data) == -1

    @overrides
    def remove(self, data):
        """ remove data from storage """
        raise NotImplementedError

    @overrides
    def remove_all(self):
        """ clear all data """
        raise NotImplementedError

    @overrides
    def uptodate(self, data):
        """ return True if data is up-to-date else False """
        raise NotImplementedError

    @overrides
    def get_more_data(self, params = {}, limit = 2000):
        """
        add new entries to database
        @limit - max num of records to add
        @params - search query
        """
        raise NotImplementedError

    @overrides
    def validate(self, data):
        """
        :param data: validate
        :return: True if data contains all keys
        """

        if not isinstance(data, JoinSongArtistNoVideo) \
                and not isinstance(data, JoinSongArtist):
            raise TypeError("data must be of type JoinSongArtist or JoinSongArtistNoVideo")

        keys = self._keys.values()
        _json = data.json()

        # if data doesn't have all required keys return False
        for v in keys:
            if not hasattr(data, v['key']):
                return False

        return True

    def _load_itunes_results(self, folder, limit = 20000):
        """ fetch all itunes data from local folder """
        itunes = []

        for dirName, subdirList, fileList in os.walk(folder):

            for _file in fileList:
                if not _file.endswith(".txt") and not _file.endswith(".text"): continue

                with open(folder + os.sep + _file, 'r') as _f:

                    # merge all results to one list
                    itunes.extend(json.load(_f)['results'])

                if len(itunes) >= limit:
                    break

        return [JoinSongArtist(**mysql_entry) for entry in itunes for mysql_entry in self._split(entry) if self._validate_itunes_api_data(entry)]

    def _split(self, entry):
        """ split each entry to num of entries according to keys """
        if not isinstance(entry, dict):
            raise TypeError("entry must be of type dict")

        mysql_entry = self._entry_to_mysql(entry)

        entries = [mysql_entry]

        for entry_keys in self._additional_entries:
            new_entry = mysql_entry.copy()

            # validate
            valid = True

            # replacing existing keys with additional
            for k, v in entry_keys.iteritems():
                # if not enough data to split, skip
                if entry.get(k, None) == None:
                    valid = False
                    break

                # update new entry data
                new_entry[v['key']] = self._parse(v, k, entry)

            # add to final entries
            if valid:
                entries.append(new_entry)

        return entries

    def _entry_to_mysql(self, entry):
        """ convert entry to mysql data keys """

        keys = self._keys.copy()
        keys.update(self._optional_keys)

        return { v['key'] : self._parse(v, k, entry) for k,v in keys.iteritems() if entry.get(k, None) != None }

    def _parse(self, v, k, entry):
        """ parse k according to v parser """
        return v['parser']().parse(entry[k])


    def _validate_itunes_api_data(self, data):
        """ make sure data is consistent with mysql relation structure """

        # make sure data contains all required keys

        for key in self._keys.keys():
            if data.get(key, None) == None:
                return False

        return True


