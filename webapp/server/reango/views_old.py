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
from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
import random

from equalizer.lib.api.mysql import MysqlApi
from equalizer.lib.storage.mysql import MySqlEngine

from equalizer import config as app

class GenericView(View):
    def params_to_dict(self, params = {}):
        """ parsing request params """
        return { k : v for k,v in params.iteritems() }

    @method_decorator(csrf_exempt, name='dispatch')
    def dispatch(self, request, *args, **kwargs):
        return super(GenericView, self).dispatch(request, *args, **kwargs)

    def get_resource(self, request, query, *args, **kwargs):
        # prepare storage engine
        engine = MySqlEngine(**app.MYSQL_INFO)

        # fetching params from request
        params = self.params_to_dict(request.GET)

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

    def get_random_genre(self, request, *args, **kwargs):
        genres = self.get_resource(request, query=app.SELECT_GENRE, *args, **kwargs).get('content', {}).get('data', [])
        random.shuffle(genres)
        return genres[0]['genre']

    def get_random_year(self, request, *args, **kwargs):
        years = self.get_resource(request, query=app.SELECT_YEAR, *args, **kwargs).get('content', {}).get('data', [])
        random.shuffle(years)
        return years[0]['year']

    def get_random_country(self, request, *args, **kwargs):
        countries = self.get_resource(request, query=app.SELECT_COUNTRY, *args, **kwargs).get('content', {}).get('data', [])
        random.shuffle(countries)
        return countries[0]['country']

    def req_to_mutable(self, request):
        # making params mutable
        params = QueryDict('', mutable=True)
        params.update({k: v for k, v in request.GET.iteritems()})
        request.GET = params

    def get(self, request, query, *args, **kwargs):
        response = self.get_resource(request, query, *args, **kwargs)

        return HttpResponse(json.dumps(response), content_type='application/json')

    def post(self, request, query, *args, **kwargs):
        response = self.post_resource(request, query, *args, **kwargs)

        return HttpResponse(json.dumps(response), content_type='application/json')

class LoginView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(LoginView, self).get(request, query=app.LOGIN_AUTH, *args, **kwargs)

class SignUpView(GenericView):
    def post(self, request, *args, **kwargs):
        """ executing sign up request """
        return super(SignUpView, self).post(request, query=app.SIGN_USER, *args, **kwargs)

class MostUnlikedSongView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return most unliked songs in genre from db """
        self.req_to_mutable(request)

        # getting random year
        request.GET['year'] = self.get_random_year(request)

        return super(MostUnlikedSongView, self).get(request, query=app.MOST_UNLIKED_SONGS, *args, **kwargs)

class DislikedSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return most hated songs in year """
        return super(DislikedSongsView, self).get(request, query=app.DISLIKED_SONGS, *args, **kwargs)

class MostLikedSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return most liked songs """

        self.req_to_mutable(request)

        # getting random year
        request.GET['year'] = self.get_random_year(request)

        return super(MostLikedSongsView, self).get(request, query=app.MOST_LIKED_SONGS, *args, **kwargs)

class RelevantArtistView(GenericView) :
    def get(self, request, *args, **kwargs):
        """ executing login request """
        self.req_to_mutable(request)

        # setting random genre
        request.GET['genre'] = self.get_random_genre(request, *args, **kwargs)

        # return http response
        return super(RelevantArtistView, self).get_resource(request, query=app.RELEVANT_ARTIST_SONGS, *args, **kwargs)

class EqualizerView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """

        self.req_to_mutable(request)

        # getting random genre
        request.GET['genre'] = self.get_random_genre(request, *args, **kwargs)

        # getting random country
        request.GET['country'] = self.get_random_country(request, *args, **kwargs)

        # prepare equalizer user params
        keys = ['likes', 'dislikes', 'views', 'comments']
        keys = [(k , float(request.GET[k])) for k in keys]
        for k, v in keys: request.GET[k] = v

        # normalizing user params
        norm = float(sum(map(lambda (x,y) : y , keys)))

        for k, v in keys: request.GET[k] = float(v/norm)

        # executing equalizer logics
        response = self.get_resource(request, query = app.EQUALIZER, *args, **kwargs)
        response['title'] = "Custom search : %.2f likes, %.2f dislikes, %.2f views, %.2f comments " %tuple(request.GET[k] for k,v in keys)

        return HttpResponse(json.dumps(response), content_type='application/json')

class LongestArtistSongView(GenericView) :
    def get(self, request, *args, **kwargs):
        """ return artist with longest songs average """
        return super(LongestArtistSongView, self).get(request, query=app.LONGEST_ARTIST_SONG, *args, **kwargs)

class PopularSongsView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return most popular songs """
        return super(PopularSongsView, self).get(request, query=app.MOST_POPULAR_SONGS, *args, **kwargs)

class HatedGenreSongView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return most hated song in year """
        self.req_to_mutable(request)

        # getting random year
        request.GET['year'] = self.get_random_year(request)

        return super(HatedGenreSongView, self).get(request, query=app.HATED_GENRE_SONGS, *args, **kwargs)

class RandomQueryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return random query """
        title, query, keys = self.get_random_query()

        print title, query, keys

        self.req_to_mutable(request)

        # get required keys
        request.GET['genre'] = self.get_random_genre(request)
        request.GET['country'] = self.get_random_country(request)
        request.GET['year'] = self.get_random_year(request)

        # execute query
        res = self.get_resource(request, query = query, *args, **kwargs)

        # add title
        res['title'] = title %request.GET[keys] if keys != None else title

        # add search results to history
        if ((res.get('content',{}).get('data',{})[0].get('count',-1)) >= 0) :
            super(RandomQueryView, self).get_resource(request, query=app.USER_HISTORY_COUNT, *args, **kwargs)
            super(RandomQueryView, self).get_resource(request, query=app.USER_HISTORY_INSERT, *args, **kwargs)
            super(RandomQueryView, self).get_resource(request, query=app.MIDDLE_HISTORY_INSERT, *args, **kwargs)

        return HttpResponse(json.dumps(res), content_type='application/json')

    def get_random_query(self):
        """ get random query """

        queries_dic = {
                        'The Most Hated Songs In Genre "%s"': {
                            'query':app.HATED_GENRE_SONGS,
                            'keys':'genre'
                        },

                        'The Most Popular Songs In Genre "%s"':{
                            'query':app.MOST_POPULAR_SONGS,
                            'keys':'genre'
                        },

                        'The Songs Of The Most Verbose Artist "%s"':{
                            'query':  app.LONGEST_ARTIST_SONG,
                            'keys' : 'genre'
                        },

                        'The Most Relevant Songs Of Artists From Genre "%s""':{
                            'query':app.RELEVANT_ARTIST_SONGS,
                            'keys':'genre'
                        },

                        'The Most Popular Songs In Year "%d"':{
                            'query':app.MOST_LIKED_SONGS,
                            'keys':'year'
                        },

                        'The Most Unliked Songs': {
                            'query': app.DISLIKES_SONGS,
                        },

                        'The Most Hated Songs In Year "%d"':{
                            'query':app.MOST_UNLIKED_SONGS,
                            'keys':'year'
                        }
                    }

        keys = queries_dic.keys()
        random.shuffle(keys)
        return (keys[0], queries_dic[keys[0]]['query'], queries_dic[keys[0]].get('keys', None))

class SearchHistoryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(SearchHistoryView, self).get(request, query=app.SEARCH_IN_HISTORY, *args, **kwargs)


class ShowHistoryPageView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """
        return super(ShowHistoryPageView, self).get(request, query=app.SHOW_HISTORY_PAGE, *args, **kwargs)
