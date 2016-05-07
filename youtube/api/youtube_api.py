__author__ = 'Saleem Latif'

from apiclient.discovery import build
from apiclient.errors import HttpError


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
