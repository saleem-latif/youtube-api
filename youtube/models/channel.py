__author__ = 'Saleem Latif'

from youtube.models.base import Base, Thumbnail
from datetime import datetime


class ChannelsResult(Base):
    """
    This model can be used as modal layer for Channels API
    """
    kind = ''
    etag = ''

    next_page = None
    total_results = None
    results_per_page = None

    channels = []

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.next_page = kwargs.get("next_page", "")
        self.total_results = kwargs.get("total_results", 0)
        self.results_per_page = kwargs.get("results_per_page", 0)

        self.channels = kwargs.get("channels", [])

    @classmethod
    def from_channels_result(cls, result):
        channels = map(lambda item: Channel.from_channels_result(item), result.items)

        channel_result = ChannelsResult(
            kind=result.kind,
            etag=result.etag,
            channels=channels,
            next_page=result.next_page_token,
            total_results=result.total_results,
            results_per_page=result.results_per_page,
        )
        return channel_result


class Channel(Base):
    """

    """
    kind = ''
    etag = ''

    channel_id = ''
    title = ''
    description = ''
    custom_url = ''

    publish_date = None
    thumbnail = None

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.channel_id = kwargs.get("channel_id", '')
        self.title = kwargs.get("title", '')
        self.description = kwargs.get("description", "")
        self.custom_url = kwargs.get("custom_url", "#")

        self.publish_date = kwargs.get("publish_date", datetime.now())
        self.thumbnail = kwargs.get("thumbnail", None)

    @property
    def id(self):
        return self.channel_id

    @classmethod
    def from_search_result(cls, result):
        return Channel(
            channel_id=result.channel_id,
            kind=result.kind,
            etag=result.etag,
            title=result.channel_title,
            description=result.description,
            publish_date=result.published_at,
            thumbnail=Thumbnail.from_parser(result.thumbnails),
        )

    @classmethod
    def from_channels_result(cls, result):
        return Channel(
            channel_id=result.id,
            kind=result.kind,
            etag=result.etag,
            title=result.title,
            description=result.description,
            publish_date=result.published_at,
            custom_url=result.custom_url,
            thumbnail=Thumbnail.from_parser(result.thumbnails),
        )

