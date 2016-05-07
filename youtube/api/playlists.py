__author__ = 'Saleem Latif'

from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.playlist import PlaylistListResponseParser


class Playlists(APIBase):
    """

    """
    params = {
        "part": "id,snippet",
        "maxResults": MAX_RESULT
    }

    def __init__(self, youtube, **kwargs):
        self.params.update(kwargs)
        super(Playlists, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        return PlaylistListResponseParser(self.fetch())

    def fetch(self):
        return self.youtube.api.playlists().list(**self.params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))

    def order_by(self, order):
        self.params.update(order=order)
        return self()
