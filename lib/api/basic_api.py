from .api_interface import Api

import requests

class BasicApi(Api):
    def __init__(self, url, params):
        self.__request = requests.Request(url = url, params = params, method = 'GET')

    def get(self):
        req = self.__request.prepare()
        session = requests.Session()
        res = session.send(req).json()
        session.close()
        return res

    def info(self):
        return self.__dict__

    def set(self, key, val):
        self.__request.params[key] = val

    def set_url(self, url):
        self.__request.url = url

    def get_url(self):
        return self.__request.url

    def get_full_url(self):
        return self.__request.prepare().url
