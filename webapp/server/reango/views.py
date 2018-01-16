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

from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import redirect

from equalizer.lib.api.mysql import MysqlApi
from equalizer.lib.storage.mysql import MySqlEngine

import json
from equalizer import config as app
import random

class GenericView(View):
    def params_to_dict(self, params = {}):
        """ parsing request params """
        return { k : v for k,v in params.iteritems() if len(v) > 0 }

    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        return super(GenericView, self).dispatch(request, *args, **kwargs)

    def get_resource(self, request, query, *args, **kwargs):
        # prepare storage engine
        engine = MySqlEngine(**app.MYSQL_INFO)

        # fetching params from request
        params = self.params_to_dict(request.GET)
        print(params ,"my params ")

        # execute query
        mysql_api = MysqlApi(engine=engine)
        return mysql_api.execute(params=params, **query)

    def post_resource(self, request, query, *args, **kwargs):
        # prepare storage engine
        engine = MySqlEngine(**app.MYSQL_INFO)

        try:
            params = json.loads(request.body)
        except:
            return HttpResponse(
                json.dumps({'rc': -1, 'errorMsg': 'post data json isn\'t legal'}),
                content_type='application/json')

        # execute query
        mysql_api = MysqlApi(engine=engine)

        return mysql_api.execute(params=params, **query)

    def get(self, request, query, *args, **kwargs):
        response = self.get_resource(request, query, *args, **kwargs)
        print response

        return HttpResponse(json.dumps(response), content_type='application/json')

    def post(self, request, query, *args, **kwargs):
        response = self.post_resource(request, query, *args, **kwargs)

        return HttpResponse(json.dumps(response), content_type='application/json')


class LoginView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(LoginView, self).get(request, query=app.USER_LOGIN, *args, **kwargs)


class SignUpView(GenericView):
    def post(self, request, *args, **kwargs):
        """ executing login request """
        return super(SignUpView, self).post(request, query=app.USER_SIGN_UP, *args, **kwargs)


class MostUnlikedSongView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(MostUnlikedSongView, self).get(request, query=app.MOST_UNLIKED_SONGS, *args, **kwargs)

class DislikeSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(DislikeSongsView, self).get(request, query=app.DISLIKES_SONGS, *args, **kwargs)


class MostLikedSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(MostLikedSongsView, self).get(request, query=app.MOST_LIKED_SONGS, *args, **kwargs)

class RelevantArtistView(GenericView) :
    def get(self, request, *args, **kwargs):
        """ executing login request """
        response = self.get_resource(request, query=app.RELEVANT_ARTIST_SONGS, *args, **kwargs)
        print response
        return HttpResponse(json.dumps(response), content_type='application/json')

    def get_resource(self, request, query, *args, **kwargs):
        _sql_genre = super(RelevantArtistView, self).get_resource(request, query=app.SELECT_GENRE, *args, **kwargs)
        random.shuffle(_sql_genre)
        genre = [item['genre'] for item in _sql_genre][0]
        request.GET['genre'] = genre
        return super(RelevantArtistView, self).get_resource(request, query=app.RELEVANT_ARTIST_SONGS, *args, **kwargs)

class EqualizerView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        _sql_genre = super(EqualizerView, self).get_resource(request, query=app.SELECT_GENRE, *args, **kwargs)
        random.shuffle(_sql_genre)
        genre = [item['genre'] for item in _sql_genre][0]
        request.GET['genre']=genre
        _sql_country = super(EqualizerView, self).get_resource(request, query=app.SELECT_COUNTRY, *args, **kwargs)
        random.shuffle(_sql_country)
        country = [item['country'] for item in _sql_genre][0]
        request.GET['country']=country
        return super(EqualizerView, self).get(request, query=app.EQUALIZER, *args, **kwargs)


class LongestArtistSongView(GenericView) :
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(LongestArtistSongView, self).get(request, query=app.LONGEST_ARTIST_SONG, *args, **kwargs)


class PopularSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(PopularSongsView, self).get(request, query=app.MOST_POPULAR_SONGS, *args, **kwargs)


class HatedGenreSongView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(HatedGenreSongView, self).get(request, query=app.HATED_GENRE_SONGS, *args, **kwargs)

class RandomQueryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        queries_dic = {'The Most Hated Songs In Genre "%s"':{'query':app.HATED_GENRE_SONGS,'keys':'genre'},
                       'The Most Popular Songs In Genre "%s"':{'query':app.MOST_POPULAR_SONGS,'keys':'genre'},
                       'The Songs Of The Most Verbose Artist "%s"':app.LONGEST_ARTIST_SONG,
                       #'The Most Relevant Songs Of Artists From Genre "%s""':{'query':app.RELEVANT_ARTIST_SONGS,'keys':'genre'},
                       'The Most Popular Songs In Year "%d"':{'query':app.MOST_LIKED_SONGS,'keys':'year'},
                       'The Most Unliked Songs':app.DISLIKES_SONGS,
                       'The Most Hated Songs In Year "%d"':{'query':app.MOST_UNLIKED_SONGS,'keys':'year'}}
        keys=queries_dic.keys()
        random.shuffle(keys)
        selected_query = keys[0]
        _ans = super(RandomQueryView, self).get_resource(request, query=queries_dic[selected_query]['query'], *args, **kwargs)
        parm = ()
        if( (len(_ans.get('content',{}).get('data',{}))>0) and (len(queries_dic[selected_query].keys())>1 )):
            parm = _ans.get('content', {}).get('data', {})[0].get(queries_dic[selected_query]['keys'])
        _ans['content']['title']=selected_query % parm
        _ans = super(RandomQueryView, self).get_resource(request, query=app.USER_HISTORY_COUNT, *args, **kwargs)
        if ((_ans.get('content',{}).get('data',{})[0].get('count',-1))==0) :
            super(RandomQueryView, self).get_resource(request, query=app.USER_HISTORY_INSERT, *args, **kwargs)
            super(RandomQueryView, self).get_resource(request, query=app.MIDDLE_HISTORY_INSERT, *args, **kwargs)
        return HttpResponse(json.dumps(_ans), content_type='application/json')


class SearchHistoryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(SearchHistoryView, self).get(request, query=app.SEARCH_IN_HISTORY, *args, **kwargs)


class ShowHistoryPageView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(ShowHistoryPageView, self).get(request, query=app.SHOW_HISTORY_PAGE, *args, **kwargs)
