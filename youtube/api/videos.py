__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.videos import VideoListResponse

# Cache for api
cache = get_cache()


class Videos(APIBase):
    """
    This class is responsible for fetching youtube videos.
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
        return VideoListResponse(self.fetch(**self.params))

    @cache.region(region="videos")
    def fetch(self, **params):
        return self.youtube.api.videos().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
