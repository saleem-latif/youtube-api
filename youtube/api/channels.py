__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.parsers.channel import ChannelListResponse
from youtube.models.channel import ChannelsResult

from youtube.decorators import default_on_error


# Cache for api
cache = get_cache()


class Channels(APIBase):
    """
    Channels is responsible for fetching youtube API channels
    """
    def __init__(self, youtube, **kwargs):
        self.reset_params()
        self.params.update(kwargs)
        super(Channels, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        result = ChannelListResponse(self.fetch(**self.params))
        return ChannelsResult.from_channels_result(result)

    @cache.region(region="channels")
    @default_on_error((ValueError, UnicodeDecodeError), {})
    def fetch(self, **params):
        self.reset_params()
        return self.youtube.api.channels().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
