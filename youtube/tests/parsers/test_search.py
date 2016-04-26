"""
Tests for youtube-api search parsers.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase

from youtube.parsers.search import SearchResultParser, SearchResponseParser
from youtube.parsers.constants import KIND_CHANNEL, KIND_PLAYLIST, KIND_VIDEO
from youtube.tests.data.search_result import data as utf_data


class TestSearchResultParser(TestCase):
    """
    Tests for SearchResultParser.
    """

    def setUp(self):
        super(TestSearchResultParser, self).setUp()
        self.test_data_str = open("../data/search-result.json").read()
        self.test_data = json.loads(self.test_data_str)

    def test_search(self):
        data = SearchResultParser(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['id']['kind'])

        self.assertEqual(data.video_id, self.test_data['id']['videoId'])
        self.assertEqual(data.channel_id, self.test_data['id']['channelId'])
        self.assertEqual(data.playlist_id, self.test_data['id']['playlistId'])

        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.published_at, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.channel_title, self.test_data['snippet']['channelTitle'])

        self.assertEqual(data.thumbnails.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertEqual(data.thumbnails.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertEqual(data.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.thumbnails.maxres, self.test_data['snippet']['thumbnails']['maxres'])

    def test_search_utf(self):
        self.test_data = utf_data
        data = SearchResultParser(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['id']['kind'])

        self.assertEqual(data.video_id, self.test_data['id']['videoId'])
        self.assertEqual(data.channel_id, self.test_data['id']['channelId'])
        self.assertEqual(data.playlist_id, self.test_data['id']['playlistId'])

        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.published_at, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.channel_title, self.test_data['snippet']['channelTitle'])

        self.assertEqual(data.thumbnails.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertEqual(data.thumbnails.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertEqual(data.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.thumbnails.maxres, self.test_data['snippet']['thumbnails']['maxres'])


class TestSearchResponseParser(TestCase):
    """
    Tests for SearchResponseParser.
    """

    def setUp(self):
        super(TestSearchResponseParser, self).setUp()
        self.test_data_str = open("../data/search-results.json").read()
        self.test_data = json.loads(self.test_data_str)

    def test_search(self):
        data = SearchResponseParser(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])
        self.assertEqual(data.next_page_token, self.test_data['nextPageToken'])
        self.assertEqual(data.region_code, self.test_data['regionCode'])
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])

        for index, item in enumerate(data.items):
            self.assertEqual(item.etag, self.test_data['items'][index]['etag'])
            self.assertEqual(item.kind, self.test_data['items'][index]['id']['kind'])

            if item.kind == KIND_VIDEO:
                self.assertEqual(item.video_id, self.test_data['items'][index]['id']['videoId'])
            if item.kind == KIND_CHANNEL:
                self.assertEqual(item.channel_id, self.test_data['items'][index]['id']['channelId'])
            if item.kind == KIND_PLAYLIST:
                self.assertEqual(item.playlist_id, self.test_data['items'][index]['id']['playlistId'])

            self.assertEqual(item.title, self.test_data['items'][index]['snippet']['title'])
            self.assertEqual(item.published_at, self.test_data['items'][index]['snippet']['publishedAt'])
            self.assertEqual(item.description, self.test_data['items'][index]['snippet']['description'])
            self.assertEqual(item.channel_title, self.test_data['items'][index]['snippet']['channelTitle'])

            self.assertEqual(
                item.thumbnails.default,
                self.test_data['items'][index]['snippet']['thumbnails'].get('default', ''),
            )
            self.assertEqual(
                item.thumbnails.medium,
                self.test_data['items'][index]['snippet']['thumbnails'].get('medium', ''),
            )
            self.assertEqual(
                item.thumbnails.high,
                self.test_data['items'][index]['snippet']['thumbnails'].get('high', ''),
            )
            self.assertEqual(
                item.thumbnails.maxres,
                self.test_data['items'][index]['snippet']['thumbnails'].get('maxres', ''),
            )
