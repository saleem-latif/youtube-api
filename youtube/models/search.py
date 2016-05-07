__author__ = 'Saleem Latif'

from youtube.models.base import BaseModel


class SearchResultModel(BaseModel):
    """

    """
    kind = ''
    etag = ''

    videos = []
    channels = []
    playlists = []

    next_page = None
    total_results = None
    results_per_page = None

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.videos = kwargs.get("videos", [])
        self.channels = kwargs.get("channels", [])
        self.playlists = kwargs.get("playlists", [])

        self.next_page = kwargs.get("next_page", "")
        self.total_results = kwargs.get("total_results", 0)
        self.results_per_page = kwargs.get("results_per_page", 0)
