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

    def get_random_data(self, key, request):
        rand_data = {
            'year'          : self.get_random_year,
            'genre'         : self.get_random_genre,
            'country'       : self.get_random_country,
            'artist'        : self.get_random_artist,
            'years_range'   : self.get_random_years_range
        }

        return rand_data[key](request)

    def get_random_genre(self, request, *args, **kwargs):
        genres = self.get_resource(request, query=app.SELECT_RANDOM_GENRE, *args, **kwargs).get('content', {}).get('data', [])
        return {'genre' : genres[0]['genre']}

    def get_random_year(self, request, *args, **kwargs):
        years = self.get_resource(request, query=app.SELECT_RANDOM_YEAR, *args, **kwargs).get('content', {}).get('data', [])
        return {'year' : int(years[0]['year'])}

    def get_random_years_range(self, request, *args, **kwargs):
        year1 = self.get_random_year(request)['year']
        year2 = self.get_random_year(request)['year']

        year1, year2 = sorted([year1, year2])

        return {'year1': year1,'year2' : year2, 'years_range' : str(year1) + ' - ' + str(year2)}

    def get_random_country(self, request, *args, **kwargs):
        countries = self.get_resource(request, query=app.SELECT_RANDOM_COUNTRY, *args, **kwargs).get('content', {}).get('data', [])
        return {'country' : countries[0]['country']}

    def get_random_artist(self, request, *args, **kwargs):
        artists = self.get_resource(request, query=app.SELECT_RANDOM_ARTIST, *args, **kwargs).get('content', {}).get('data', [])
        return {'artist_id' : artists[0]['artist_id'], 'artist_name' : str(artists[0]['artist_name'])}

    def post_user_results(self, data, user_id):
        # prepare storage engine
        engine = MySqlEngine(**app.MYSQL_INFO)

        # execute query
        mysql_api = MysqlApi(engine=engine)

        return mysql_api.execute(params={'data' : data, 'user_id' : int(user_id)}, **app.INSERT_NEW_SEARCH_RESULTS)

    def update_user_history(self, user_id, response):
        if len(response.get('content', {}).get('data', [])) == 0: return

        user_results = ','.join([str(int(video['video_id'])) for video in response.get('content', {}).get('data', [])])

        self.post_user_results(user_results, user_id)
        self.remove_user_old_search_results(user_id)

    def remove_user_old_search_results(self, user_id):

        # prepare storage engine
        engine = MySqlEngine(**app.MYSQL_INFO)

        # execute query
        mysql_api = MysqlApi(engine=engine)

        results_count = mysql_api.execute(params={'user_id': int(user_id)}, **app.GET_USER_RESULTS_COUNT) \
            .get('content', {}).get('data', [])[0]['resultsCount']

        if int(results_count) > 20:
            recent_history = mysql_api.execute(params={'user_id': int(user_id)}, **app.GET_USER_RECENT_RESULTS) \
                .get('content', {}).get('data', [])

            result_ids = [repr(int(row['result_id'])) for row in recent_history]
            result_ids = ','.join(result_ids)

            mysql_api.execute(params={'user_id': int(user_id), 'result_ids' : result_ids}, **app.REMOVE_USER_OLD_HISTORY)

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

class EqualizerView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """

        self.req_to_mutable(request)

        # getting random genre
        request.GET['genre'] = self.get_random_genre(request, *args, **kwargs)['genre']

        # getting random country
        request.GET['country'] = self.get_random_country(request, *args, **kwargs)['country']

        # prepare equalizer user params
        keys = ['likes', 'dislikes', 'views', 'comments']
        keys = [(k , float(request.GET[k])) for k in keys]
        for k, v in keys: request.GET[k] = v

        # normalizing user params
        norm = float(sum(map(lambda (x,y) : y , keys)))

        for k, v in keys: request.GET[k] = float(v/norm)

        # executing equalizer logics
        response = self.get_resource(request, query = app.VIDEOS_CUSTOM_STATISTICS, *args, **kwargs)
        response['title'] = "Custom search : %.2f likes, %.2f dislikes, %.2f views, %.2f comments " %tuple(request.GET[k] for k,v in keys)

        # updating user history
        self.update_user_history(request.GET['user_id'], response)

        return HttpResponse(json.dumps(response), content_type='application/json')

class RandomQueryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ return random query """
        title, query, keys, rand_data = self.get_random_query()

        self.req_to_mutable(request)

        # get required keys
        for data in rand_data:
            request.GET.update(self.get_random_data(data, request))

        # execute query
        response = self.get_resource(request, query = query, *args, **kwargs)

        # add title
        response['title'] = title %repr(request.GET[keys]) if keys != None else title

        # add search results to history
        self.update_user_history(int(request.GET['user_id']), response)

        return HttpResponse(json.dumps(response), content_type='application/json')

    def get_random_query(self):
        """ get random query """

        queries_dic = {
                        'Most ambivalent songs of artist "%s"': {
                            'query' : app.MOST_AMBIVALENT_SONGS_OF_ARTIST,
                            'keys'  :'artist_name',
                            'rand_data': ['artist']
                        },

                        'Most hated artists between %s': {
                            'query': app.MOST_HATED_ARTISTS_OF_YEAR_RANGE,
                            'keys': 'years_range',
                            'rand_data': ['years_range']
                        },

                        'Songs of artist with longest songs average in genre "%s"':{
                            'query':  app.ARTIST_WITH_LONGEST_SONGS_AVG_IN_GENRE,
                            'keys' : 'genre',
                            'rand_data': ['genre']
                        },

                        'Songs of most relevant artist in genre "%s""':{
                            'query':app.MOST_RELEVANT_ARTISTS_GENRE_SONGS,
                            'keys':'genre',
                            'rand_data' : ['genre']
                        },

                        'List from country "%s" which are of the most common genre ':{
                            'query':app.MOST_COMMON_GENRE_IN_COUNTRY,
                            'keys':'country',
                            'rand_data': ['country']
                        },

                        'Songs of most hated pair of artists in genre "%s"': {
                            'query': app.MOST_HATED_PAIR_FROM_GENRE,
                            'keys' : 'genre',
                            'rand_data': ['genre']
                        },

                        'List of most and least popular songs': {
                            'query': app.MOST_POPULAR_SONGS,
                        },

                        'List of most hated songs of %s ': {
                            'query': app.MOST_HATED_SONGS_OF_YEAR,
                            'keys': 'year',
                            'rand_data': ['year']
                        },

                        'Songs from most hated genre': {
                            'query': app.MOST_HATED_GENRE_SONGS,
                        },
                    }

        keys = queries_dic.keys()
        random.shuffle(keys)

        print (keys[0], queries_dic[keys[0]]['query'], queries_dic[keys[0]].get('keys', None), queries_dic[keys[0]].get('rand_data', []))

        return (keys[0], queries_dic[keys[0]]['query'], queries_dic[keys[0]].get('keys', None), queries_dic[keys[0]].get('rand_data', []))

class UserSearchHistoryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing search history fulltext string request """
        self.req_to_mutable(request)
        request.GET['user_id'] = int(request.GET.get('user_id', -1))

        return super(UserSearchHistoryView, self).get(request, query=app.FULLTEXT_SEARCH_IN_HISTORY, *args, **kwargs)

class UserRecentHistoryView(GenericView):
    def get(self, request, *args, **kwargs):
        """ executing login request """

        self.req_to_mutable(request)
        request.GET['user_id'] = int(request.GET.get('user_id', -1))

        return super(UserRecentHistoryView, self).get(request, query=app.GET_USER_RECENT_HISTORY, *args, **kwargs)
