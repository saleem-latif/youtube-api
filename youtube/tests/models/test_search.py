"""
Tests for youtube-api search api.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.search import SearchResponse as SearchResponseParser
from youtube.models.search import SearchResult as SearchResultModel
from youtube.parsers.constants import KIND_CHANNEL, KIND_PLAYLIST, KIND_VIDEO


class TestSearchResult(TestCase):
    """
    Tests for Search API.
    """

    def setUp(self):
        super(TestSearchResult, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/search.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_search(self):
        parsed_data = SearchResponseParser(self.test_data)
        data = SearchResultModel.from_search_result(parsed_data)

        parsed_videos = filter(lambda item: item['id']['kind'] == KIND_VIDEO, self.test_data['items'])
        parsed_channels = filter(lambda item: item['id']['kind'] == KIND_CHANNEL, self.test_data['items'])
        parsed_playlists = filter(lambda item: item['id']['kind'] == KIND_PLAYLIST, self.test_data['items'])

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(len(data.videos), len(parsed_videos))
        self.assertEqual(len(data.playlists), len(parsed_playlists))
        self.assertEqual(len(data.channels), len(parsed_channels))

        self.assertEqual(data.next_page, self.test_data['nextPageToken'])
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])
