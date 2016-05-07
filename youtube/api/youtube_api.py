__author__ = 'Saleem Latif'

from apiclient.discovery import build
from apiclient.errors import HttpError

from youtube.api.search import Search
from youtube.api.videos import Videos
from youtube.api.playlists import Playlists
from youtube.api.channels import Channels


class Youtube(object):
    """

    """
    developer_key = None
    service_name = 'youtube'
    api_version = 'v3'

    def __init__(self, developer_key, service_name='youtube', api_version='v3'):
        self.developer_key = developer_key
        self.service_name = service_name
        self.api_version = api_version

        self.api = build(self.service_name, self.api_version, developerKey=self.developer_key)

    @property
    def search(self):
        return Search(self)

    @property
    def videos(self):
        return Videos(self)

    @property
    def channels(self):
        return Channels(self)

    @property
    def playlists(self):
        return Playlists(self)
