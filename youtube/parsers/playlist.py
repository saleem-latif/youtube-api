"""
Youtube data Parsers for youtube data api for playlists.
"""
__author__ = 'Saleem Latif'

from youtube.parsers.parser import ResponseParser, ThumbnailsParser
from youtube.decorators import default_on_error


class PlaylistListResponse(ResponseParser):
    """
    Youtube data api gives the ability to fetch youtube playlists with playlists/list api endpoint.
    Result is paginated with Pagination info (such as total results, results per page, next page token etc.) included
    in the response.
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
        return map(lambda item: Playlist(item), self.result['items'])


class Playlist(ResponseParser):
    """
    Parser for Youtube API's search result,
    more info about videos api https://developers.google.com/youtube/v3/docs/playlists/list
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
    @default_on_error(KeyError, '')
    def id(self):
        return self.result['id']['playlistId']

    @property
    @default_on_error(KeyError, '')
    def channel_id(self):
        return self.result['snippet']['channelId']

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
