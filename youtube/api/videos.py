__author__ = 'Saleem Latif'

from youtube.cache import get_cache
from youtube.api.base import APIBase
from youtube.parsers.videos import VideoListResponse
from youtube.models.video import VideosResult

# Cache for api
cache = get_cache()


class Videos(APIBase):
    """
    This class is responsible for fetching youtube videos.
    """
    def __init__(self, youtube, **kwargs):
        self.reset_params()
        self.params.update(kwargs)
        super(Videos, self).__init__(youtube)

    def __call__(self, **kwargs):
        self.params.update(kwargs)
        result = VideoListResponse(self.fetch(**self.params))
        return VideosResult.from_videos_result(result)

    @cache.region(region="videos")
    def fetch(self, **params):
        self.reset_params()
        return self.youtube.api.videos().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
