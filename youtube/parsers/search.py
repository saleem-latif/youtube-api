"""

"""
__author__ = 'Saleem Latif'

from youtube.parsers.parser import BaseParser, ThumbnailsParser
from youtube.decorators import default_on_error


class SearchResponseParser(BaseParser):
    """

    """
    @property
    @default_on_error(KeyError, '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error(KeyError, '')
    def kind(self):
        return self.result['kind']

    @property
    @default_on_error(KeyError, None)
    def next_page_token(self):
        return self.result['nextPageToken']

    @property
    @default_on_error(KeyError, '')
    def region_code(self):
        return self.result['regionCode']

    @property
    @default_on_error(KeyError, 1)
    def total_results(self):
        return self.result['pageInfo']['totalResults']

    @property
    @default_on_error(KeyError, 1)
    def results_per_page(self):
        return self.result['pageInfo']['resultsPerPage']

    @property
    def items(self):
        for item in self.result['items']:
            yield SearchResultParser(item)


class SearchResultParser(BaseParser):
    """
    Parser for Youtube API's search result,
    more info about search api https://developers.google.com/youtube/v3/docs/search/list
    """
    @property
    @default_on_error(KeyError, '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error(KeyError, '')
    def kind(self):
        return self.result['id']['kind']

    @property
    @default_on_error(KeyError, '')
    def video_id(self):
        return self.result['id']['videoId']

    @property
    @default_on_error(KeyError, '')
    def channel_id(self):
        return self.result['id']['channelId']

    @property
    @default_on_error(KeyError, '')
    def playlist_id(self):
        return self.result['id']['playlistId']

    @property
    @default_on_error(KeyError, '')
    def title(self):
        return self.result['snippet']['title']

    @property
    @default_on_error(KeyError, '')
    def description(self):
        return self.result['snippet']['description']

    @property
    @default_on_error(KeyError, '')
    def channel_title(self):
        return self.result['snippet']['channelTitle']

    @property
    @default_on_error(KeyError, '')
    def published_at(self):
        return self.result['snippet']['publishedAt']

    @property
    @default_on_error(KeyError, '')
    def thumbnails(self):
        return ThumbnailsParser(self.result['snippet']['thumbnails'])
