__author__ = 'Saleem Latif'

from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.channel import ChannelsResponseParser


class Channels(APIBase):
    """

    """
    params = {
        "part": "id,snippet",
        "maxResults": MAX_RESULT
    }

    def __init__(self, youtube, **kwargs):
        self.params.update(kwargs)
        super(Channels, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        return ChannelsResponseParser(self.fetch())

    def fetch(self):
        return self.youtube.api.channels().list(**self.params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
