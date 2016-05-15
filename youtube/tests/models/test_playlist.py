"""
Tests for youtube-api Playlist model.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.playlist import PlaylistListResponse as PlaylistResponseParser, Playlist as PlaylistItemParser
from youtube.parsers.search import SearchResult
from youtube.models.playlist import PlaylistsResult as PlaylistsResultModel, Playlist
from youtube.parsers.constants import KIND_PLAYLIST


class TestPlaylistResult(TestCase):
    """
    Tests for Playlist model.
    """

    def setUp(self):
        super(TestPlaylistResult, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/playlist.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        parsed_data = PlaylistResponseParser(self.test_data)
        data = PlaylistsResultModel.from_playlists_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(len(data.playlists), len(self.test_data['items']))

        self.assertEqual(data.next_page, self.test_data['nextPageToken'])
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])


class TestPlaylist(TestCase):
    """
    Tests for Playlist model.
    """

    def setUp(self):
        super(TestPlaylist, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/playlist.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        self.test_data = self.test_data['items'][0]
        parsed_data = PlaylistItemParser(self.test_data)
        data = Playlist.from_playlists_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(data.playlist_id, self.test_data['id']['playlistId'])
        self.assertEqual(data.id, self.test_data['id']['playlistId'])
        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.publish_date, self.test_data['snippet']['publishedAt'])

        self.assertEqual(data.channel.channel_id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel.id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel.title, self.test_data['snippet']['channelTitle'])

        self.assertIsNotNone(data.thumbnail)
        self.assertIsNotNone(data.thumbnail.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertIsNotNone(data.thumbnail.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertIsNotNone(data.thumbnail.high, self.test_data['snippet']['thumbnails']['high'])

    def test_model_search_api_data(self):
        test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/playlist.json"
        ).read()
        test_data = json.loads(test_data_str)

        self.test_data = filter(lambda item: item['id']['kind'] == KIND_PLAYLIST, test_data['items'])[0]

        parsed_data = SearchResult(self.test_data)
        data = Playlist.from_search_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['id']['kind'])

        self.assertEqual(data.playlist_id, self.test_data['id']['playlistId'])
        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.publish_date, self.test_data['snippet']['publishedAt'])

        self.assertEqual(data.channel.channel_id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel.id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel.title, self.test_data['snippet']['channelTitle'])

        self.assertIsNotNone(data.thumbnail)
        self.assertIsNotNone(data.thumbnail.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertIsNotNone(data.thumbnail.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertIsNotNone(data.thumbnail.high, self.test_data['snippet']['thumbnails']['high'])
