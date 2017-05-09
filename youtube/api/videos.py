__author__ = 'Saleem Latif'

from httplib import ResponseNotReady, IncompleteRead
from httplib2 import FailedToDecompressContent
from googleapiclient.errors import HttpError

from youtube.api.base import APIBase
from youtube.parsers.videos import VideoListResponse
from youtube.models.video import VideosResult

from youtube.decorators import default_on_error


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

    @default_on_error(
        (
            ValueError, UnicodeDecodeError, AttributeError, IncompleteRead,
            ResponseNotReady, HttpError, FailedToDecompressContent,
        ),
        {}
    )
    def fetch(self, **params):
        self.reset_params()
        return self.youtube.api.videos().list(**params).execute()

    @property
    def cache_key(self):
        return hash(frozenset(self.params.items()))
