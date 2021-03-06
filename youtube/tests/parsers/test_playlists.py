"""
Tests for youtube-api search parsers.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.playlist import Playlist, PlaylistListResponse
from youtube.tests.data.playlist_result import data as utf_data


class TestPlaylistItemParser(TestCase):
    """
    Tests for VideoListItemParser.
    """

    def setUp(self):
        super(TestPlaylistItemParser, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/playlist-result.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_videos(self):
        data = Playlist(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(data.id, self.test_data['id']['playlistId'])
        self.assertEqual(data.channel_id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel_title, self.test_data['snippet']['channelTitle'])

        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.published_at, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])

        self.assertEqual(data.thumbnails.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertEqual(data.thumbnails.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertEqual(data.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])

    def test_videos_utf(self):
        self.test_data = utf_data
        data = Playlist(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(data.id, self.test_data['id']['playlistId'])
        self.assertEqual(data.channel_id, self.test_data['snippet']['channelId'])
        self.assertEqual(data.channel_title, self.test_data['snippet']['channelTitle'])

        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.published_at, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])

        self.assertEqual(data.thumbnails.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertEqual(data.thumbnails.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertEqual(data.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.thumbnails.maxres, self.test_data['snippet']['thumbnails']['maxres'])


class TestPlaylistResponseParser(TestCase):
    """
    Tests for VideoListResponse.
    """

    def setUp(self):
        super(TestPlaylistResponseParser, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/playlist-results.json",
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_videos(self):
        data = PlaylistListResponse(self.test_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])
        self.assertEqual(data.next_page_token, self.test_data.get('nextPageToken', None))
        self.assertEqual(data.region_code, self.test_data.get('regionCode', ''))
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])

        for index, item in enumerate(data.items):
            self.assertEqual(item.etag, self.test_data['items'][index]['etag'])
            self.assertEqual(item.kind, self.test_data['items'][index]['kind'])
            self.assertEqual(item.id, self.test_data['items'][index]['id']['playlistId'])
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
