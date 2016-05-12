__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.api.contants import MAX_RESULT
from youtube.parsers.search import SearchResponse

# Cache for api
cache = get_cache()


class Search(APIBase):
    """
    This class is responsible for searching youtube content.
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
        search_response = self.fetch(**self.params)
        return SearchResponse(search_response)

    @cache.region(region="search")
    def fetch(self, **params):
        return self.youtube.api.search().list(**params).execute()

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
