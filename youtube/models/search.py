__author__ = 'Saleem Latif'

from youtube.models.base import Base
from youtube.models.video import Video
from youtube.models.channel import Channel
from youtube.models.playlist import Playlist
from youtube.parsers.constants import KIND_VIDEO, KIND_PLAYLIST, KIND_CHANNEL


class SearchResult(Base):
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

    @classmethod
    def from_search_result(cls, result):
        parsed_videos = filter(lambda item: item.kind == KIND_VIDEO, result.items)
        parsed_channels = filter(lambda item: item.kind == KIND_CHANNEL, result.items)
        parsed_playlists = filter(lambda item: item.kind == KIND_PLAYLIST, result.items)

        videos = map(lambda item: Video.from_search_result(item), parsed_videos)
        channels = map(lambda item: Channel.from_search_result(item), parsed_channels)
        playlists = map(lambda item: Playlist.from_search_result(item), parsed_playlists)

        search = SearchResult(
            kind=result.kind,
            etag=result.etag,
            videos=videos,
            channels=channels,
            playlists=playlists,
            next_page=result.next_page_token,
            total_results=result.total_results,
            results_per_page=result.results_per_page,
        )
        return search
