__author__ = 'Saleem Latif'

from youtube.models.base import Base
from datetime import datetime


class Channel(Base):
    """

    """
    kind = ''
    etag = ''

    channel_id = ''
    title = ''
    description = ''

    publish_date = None
    thumbnail = None

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.channel_id = kwargs.get("channel_id", '')
        self.title = kwargs.get("title", '')
        self.description = kwargs.get("description", "")

        self.channel = kwargs.get("channel", None)
        self.publish_date = kwargs.get("publish_date", datetime.now())
        self.thumbnail = kwargs.get("thumbnail", None)

    @property
    def id(self):
        return self.channel_id
