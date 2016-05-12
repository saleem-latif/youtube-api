__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.playlist import PlaylistListResponse

# Cache for api
cache = get_cache()


class Playlists(APIBase):
    """
    This class is responsible for fetching youtube Playlists
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
        return PlaylistListResponse(self.fetch(**self.params))

    @cache.region(region="playlists")
    def fetch(self, **params):
        return self.youtube.api.playlists().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
