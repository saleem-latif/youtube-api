__author__ = 'Saleem Latif'

from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.search import SearchResponseParser


class Search(APIBase):
    """

    """
    params = {
        "part": "id,snippet",
        "maxResults": MAX_RESULT
    }

    def __init__(self, youtube, **kwargs):
        self.params.update(kwargs)
        super(Search, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        search_response = self.fetch()
        return SearchResponseParser(search_response)

    def fetch(self):
        return self.youtube.api.search().list(**self.params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))

    @property
    def videos(self):
        self.params.update(type='video')
        return self

    @property
    def channels(self):
        self.params.update(type='channel')
        return self

    @property
    def playlist(self):
        self.params.update(type='playlist')
        return self
