__author__ = 'Saleem Latif'

from youtube.models.base import Base, Thumbnail
from youtube.models.channel import Channel
from datetime import datetime


class VideosResult(Base):
    """
    This model can be used as modal layer for Channels API
    """
    kind = ''
    etag = ''

    next_page = None
    total_results = None
    results_per_page = None

    videos = []

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.next_page = kwargs.get("next_page", "")
        self.total_results = kwargs.get("total_results", 0)
        self.results_per_page = kwargs.get("results_per_page", 0)

        self.videos = kwargs.get("videos", [])

    @classmethod
    def from_videos_result(cls, result):
        videos = map(lambda item: Video.from_videos_result(item), result.items)

        videos_result = VideosResult(
            kind=result.kind,
            etag=result.etag,
            videos=videos,
            next_page=result.next_page_token,
            total_results=result.total_results,
            results_per_page=result.results_per_page,
        )
        return videos_result


class Video(Base):
    """

    """
    kind = ''
    etag = ''

    video_id = ''
    title = ''
    description = ''

    channel = None
    publish_date = None
    thumbnail = None

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.video_id = kwargs.get("video_id", '')
        self.title = kwargs.get("title", '')
        self.description = kwargs.get("description", "")

        self.channel = kwargs.get("channel", None)
        self.publish_date = kwargs.get("publish_date", datetime.now())
        self.thumbnail = kwargs.get("thumbnail", None)

    @property
    def id(self):
        return self.video_id

    @classmethod
    def from_search_result(cls, result):
        return Video(
            video_id=result.video_id,
            kind=result.kind,
            etag=result.etag,
            channel=Channel(channel_id=result.channel_id, title=result.channel_title),
            title=result.title,
            description=result.description,
            publish_date=result.published_at,
            thumbnail=Thumbnail.from_parser(result.thumbnails),
        )

    @classmethod
    def from_videos_result(cls, result):
        return Video(
            video_id=result.id,
            kind=result.kind,
            etag=result.etag,
            channel=Channel(channel_id=result.channel_id, title=result.channel_title),
            title=result.title,
            description=result.description,
            publish_date=result.published_at,
            thumbnail=Thumbnail.from_parser(result.thumbnails),
        )

