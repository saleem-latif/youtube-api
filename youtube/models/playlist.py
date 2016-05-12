__author__ = 'Saleem Latif'

from youtube.models.base import Base
from datetime import datetime


class PlaylistModel(Base):
    """

    """
    kind = ''
    etag = ''

    playlist_id = ''
    title = ''
    description = ''

    channel = None
    publish_date = None
    thumbnail = None

    def __init__(self, **kwargs):
        self.kind = kwargs.get("kind", "")
        self.etag = kwargs.get("etag", "")

        self.playlist_id = kwargs.get("playlist_id", '')
        self.title = kwargs.get("title", '')
        self.description = kwargs.get("description", "")

        self.channel = kwargs.get("channel", None)
        self.publish_date = kwargs.get("publish_date", datetime.now())
        self.thumbnail = kwargs.get("thumbnail", None)

    @property
    def id(self):
        return self.playlist_id
