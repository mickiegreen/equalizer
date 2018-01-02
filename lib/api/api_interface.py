class Api(object):
    def get(self):
        raise NotImplementedError

    def info(self):
        raise NotImplementedError

    def json(self):
        raise NotImplementedError

    def set(self, key, val):
        raise NotImplementedError

    def set_url(self, url):
        raise NotImplementedError

    def get_url(self):
        raise NotImplementedError

    def get_full_url(self):
        raise NotImplementedError
