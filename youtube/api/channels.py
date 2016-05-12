__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.channel import ChannelListResponse

# Cache for api
cache = get_cache()


class Channels(APIBase):
    """
    Channels is responsible for fetching youtube API channels
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
        return ChannelListResponse(self.fetch(**self.params))

    @cache.region(region="channels")
    def fetch(self, **params):
        return self.youtube.api.channels().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
