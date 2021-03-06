__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.parsers.playlist import PlaylistListResponse
from youtube.models.playlist import PlaylistsResult

from youtube.decorators import default_on_error


# Cache for api
cache = get_cache()


class Playlists(APIBase):
    """
    This class is responsible for fetching youtube Playlists
    """
    def __init__(self, youtube, **kwargs):
        self.reset_params()
        self.params.update(kwargs)
        super(Playlists, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        result = PlaylistListResponse(self.fetch(**self.params))
        return PlaylistsResult.from_playlists_result(result)

    @cache.region(region="playlists")
    @default_on_error((ValueError, UnicodeDecodeError), {})
    def fetch(self, **params):
        self.reset_params()
        return self.youtube.api.playlists().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
