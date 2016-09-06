"""
Youtube data Parsers for youtube data api for search results.
"""
__author__ = 'Saleem Latif'

from youtube.parsers.parser import ResponseParser, ThumbnailsParser
from youtube.decorators import default_on_error


class SearchResponse(ResponseParser):
    """
    Youtube data api gives the ability to search through youtube search/list api endpoint.
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
    @default_on_error((KeyError, TypeError), '')
    def region_code(self):
        return self.result['regionCode']

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
        return map(lambda item: SearchResult(item), self.result['items'])


class SearchResult(ResponseParser):
    """
    Parser for Youtube API's search result,
    more info about search api https://developers.google.com/youtube/v3/docs/search/list
    """
    @property
    @default_on_error((KeyError, TypeError), '')
    def etag(self):
        return self.result['etag']

    @property
    @default_on_error((KeyError, TypeError), '')
    def kind(self):
        return self.result['id']['kind']

    @property
    @default_on_error((KeyError, TypeError), '')
    def video_id(self):
        return self.result['id']['videoId']

    @property
    @default_on_error((KeyError, TypeError), '')
    def channel_id(self):
        try:
            return self.result['id']['channelId']
        except (KeyError, TypeError):
            return self.result['snippet']['channelId']

    @property
    @default_on_error((KeyError, TypeError), '')
    def playlist_id(self):
        return self.result['id']['playlistId']

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
    def channel_title(self):
        return self.result['snippet']['channelTitle']

    @property
    @default_on_error((KeyError, TypeError), '')
    def published_at(self):
        return self.result['snippet']['publishedAt']

    @property
    @default_on_error((KeyError, TypeError), ThumbnailsParser({}))
    def thumbnails(self):
        return ThumbnailsParser(self.result['snippet']['thumbnails'])
