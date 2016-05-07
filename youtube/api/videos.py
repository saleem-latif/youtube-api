__author__ = 'Saleem Latif'

from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.videos import VideoListResponseParser


class Videos(APIBase):
    """

    """
    params = {
        "part": "id,snippet",
        "maxResults": MAX_RESULT
    }

    def __init__(self, youtube, **kwargs):
        self.params.update(kwargs)
        super(Videos, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        return VideoListResponseParser(self.fetch())

    def fetch(self):
        return self.youtube.api.videos().list(**self.params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
