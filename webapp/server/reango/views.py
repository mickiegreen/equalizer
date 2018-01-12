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
