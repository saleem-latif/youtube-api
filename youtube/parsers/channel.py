"""
Data Parsers for youtube data api for channels.
"""
__author__ = 'Saleem Latif'

from youtube.parsers.parser import ResponseParser, ThumbnailsParser
from youtube.decorators import default_on_error


class ChannelListResponse(ResponseParser):
    """
    Youtube data api gives the ability to fetch youtube channels with channels/list api endpoint.
    Result is paginated with Pagination info (such as total results, results per page, next page token etc.) included
    in the response.
    """
    @property
    @default_on_error((KeyError, TypeError), '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error((KeyError, TypeError), '')
    def kind(self):
        return self.result['kind']

    @property
    @default_on_error((KeyError, TypeError), None)
    def next_page_token(self):
        return self.result['nextPageToken']

    @property
    @default_on_error((KeyError, TypeError), 1)
    def total_results(self):
        return self.result['pageInfo']['totalResults']

    @property
    @default_on_error((KeyError, TypeError), 1)
    def results_per_page(self):
        return self.result['pageInfo']['resultsPerPage']

    @property
    def items(self):
        return map(lambda item: Channel(item), self.result['items'])


class Channel(ResponseParser):
    """
    Parser for Youtube API's search result,
    more info about videos api https://developers.google.com/youtube/v3/docs/playlists/list
    """
    @property
    @default_on_error((KeyError, TypeError), '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error((KeyError, TypeError), '')
    def kind(self):
        return self.result['kind']

    @property
    @default_on_error((KeyError, TypeError), '')
    def id(self):
        return self.result['id']

    @property
    @default_on_error((KeyError, TypeError), '')
    def title(self):
        return self.result['snippet']['title']

    @property
    @default_on_error((KeyError, TypeError), '')
    def description(self):
        return self.result['snippet']['description']

    @property
    @default_on_error((KeyError, TypeError), '')
    def published_at(self):
        return self.result['snippet']['publishedAt']

    @property
    @default_on_error((KeyError, TypeError), '')
    def custom_url(self):
        return self.result['snippet']['customUrl']

    @property
    @default_on_error((KeyError, TypeError), ThumbnailsParser(result={}))
    def thumbnails(self):
        return ThumbnailsParser(self.result['snippet']['thumbnails'])
