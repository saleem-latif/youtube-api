# -*- coding: UTF-8 -*-
"""
Tests for youtube-api parsers.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.parser import JSONParser
from youtube.tests.data.search_result import data as utf_data


class TestJSONParser(TestCase):
    """
    Tests for JSON parsers.
    """

    def setUp(self):
        super(TestJSONParser, self).setUp()
        self.test_data_file_name = path.dirname(path.dirname(__file__)) + "/data/search-result.json"
        self.test_data_str = open(self.test_data_file_name).read()
        self.test_data = json.loads(self.test_data_str)

    def test_json(self):
        data = JSONParser(self.test_data).parse()

        self.assertEqual(data.kind, self.test_data['kind'])
        self.assertEqual(data.etag, self.test_data['etag'])

        self.assertEqual(data.id, self.test_data['id'])
        self.assertEqual(data.id.kind, self.test_data['id']['kind'])
        self.assertEqual(data.id.videoId, self.test_data['id']['videoId'])
        self.assertEqual(data.id.channelId, self.test_data['id']['channelId'])
        self.assertEqual(data.id.playlistId, self.test_data['id']['playlistId'])

        self.assertEqual(data.snippet, self.test_data['snippet'])
        self.assertEqual(data.snippet.publishedAt, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.snippet.channelId, self.test_data['snippet']['channelId'])
        self.assertEqual(data.snippet.title, self.test_data['snippet']['title'])
        self.assertEqual(data.snippet.description, self.test_data['snippet']['description'])

        self.assertEqual(data.snippet.thumbnails, self.test_data['snippet']['thumbnails'])
        self.assertEqual(data.snippet.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.snippet.thumbnails.high.url, self.test_data['snippet']['thumbnails']['high']['url'])
        self.assertEqual(data.snippet.thumbnails.high.width, self.test_data['snippet']['thumbnails']['high']['width'])
        self.assertEqual(
            data.snippet.thumbnails.high.height, self.test_data['snippet']['thumbnails']['high']['height'],
        )

        self.assertEqual(data.snippet.channelTitle, self.test_data['snippet']['channelTitle'])
        self.assertEqual(data.snippet.liveBroadcastContent, self.test_data['snippet']['liveBroadcastContent'])

    def test_str(self):
        data = JSONParser(self.test_data_str).parse()

        self.assertEqual(data.kind, self.test_data['kind'])
        self.assertEqual(data.etag, self.test_data['etag'])

        self.assertEqual(data.id, self.test_data['id'])
        self.assertEqual(data.id.kind, self.test_data['id']['kind'])
        self.assertEqual(data.id.videoId, self.test_data['id']['videoId'])
        self.assertEqual(data.id.channelId, self.test_data['id']['channelId'])
        self.assertEqual(data.id.playlistId, self.test_data['id']['playlistId'])

        self.assertEqual(data.snippet, self.test_data['snippet'])
        self.assertEqual(data.snippet.publishedAt, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.snippet.channelId, self.test_data['snippet']['channelId'])
        self.assertEqual(data.snippet.title, self.test_data['snippet']['title'])
        self.assertEqual(data.snippet.description, self.test_data['snippet']['description'])

        self.assertEqual(data.snippet.thumbnails, self.test_data['snippet']['thumbnails'])
        self.assertEqual(data.snippet.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.snippet.thumbnails.high.url, self.test_data['snippet']['thumbnails']['high']['url'])
        self.assertEqual(data.snippet.thumbnails.high.width, self.test_data['snippet']['thumbnails']['high']['width'])
        self.assertEqual(
            data.snippet.thumbnails.high.height, self.test_data['snippet']['thumbnails']['high']['height'],
        )

        self.assertEqual(data.snippet.channelTitle, self.test_data['snippet']['channelTitle'])
        self.assertEqual(data.snippet.liveBroadcastContent, self.test_data['snippet']['liveBroadcastContent'])

    def test_file(self):
        data = JSONParser(open(self.test_data_file_name)).parse()

        self.assertEqual(data.kind, self.test_data['kind'])
        self.assertEqual(data.etag, self.test_data['etag'])

        self.assertEqual(data.id, self.test_data['id'])
        self.assertEqual(data.id.kind, self.test_data['id']['kind'])
        self.assertEqual(data.id.videoId, self.test_data['id']['videoId'])
        self.assertEqual(data.id.channelId, self.test_data['id']['channelId'])
        self.assertEqual(data.id.playlistId, self.test_data['id']['playlistId'])

        self.assertEqual(data.snippet, self.test_data['snippet'])
        self.assertEqual(data.snippet.publishedAt, self.test_data['snippet']['publishedAt'])
        self.assertEqual(data.snippet.channelId, self.test_data['snippet']['channelId'])
        self.assertEqual(data.snippet.title, self.test_data['snippet']['title'])
        self.assertEqual(data.snippet.description, self.test_data['snippet']['description'])

        self.assertEqual(data.snippet.thumbnails, self.test_data['snippet']['thumbnails'])
        self.assertEqual(data.snippet.thumbnails.high, self.test_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.snippet.thumbnails.high.url, self.test_data['snippet']['thumbnails']['high']['url'])
        self.assertEqual(data.snippet.thumbnails.high.width, self.test_data['snippet']['thumbnails']['high']['width'])
        self.assertEqual(
            data.snippet.thumbnails.high.height, self.test_data['snippet']['thumbnails']['high']['height'],
        )

        self.assertEqual(data.snippet.channelTitle, self.test_data['snippet']['channelTitle'])
        self.assertEqual(data.snippet.liveBroadcastContent, self.test_data['snippet']['liveBroadcastContent'])

    def test_utf(self):
        data = JSONParser(utf_data).parse()

        self.assertEqual(data.kind, utf_data['kind'])
        self.assertEqual(data.etag, utf_data['etag'])

        self.assertEqual(data.id, utf_data['id'])
        self.assertEqual(data.id.kind, utf_data['id']['kind'])
        self.assertEqual(data.id.videoId, utf_data['id']['videoId'])
        self.assertEqual(data.id.channelId, utf_data['id']['channelId'])
        self.assertEqual(data.id.playlistId, utf_data['id']['playlistId'])

        self.assertEqual(data.snippet, utf_data['snippet'])
        self.assertEqual(data.snippet.publishedAt, utf_data['snippet']['publishedAt'])
        self.assertEqual(data.snippet.channelId, utf_data['snippet']['channelId'])
        self.assertEqual(data.snippet.title, utf_data['snippet']['title'])
        self.assertEqual(data.snippet.description, utf_data['snippet']['description'])

        self.assertEqual(data.snippet.thumbnails, utf_data['snippet']['thumbnails'])
        self.assertEqual(data.snippet.thumbnails.high, utf_data['snippet']['thumbnails']['high'])
        self.assertEqual(data.snippet.thumbnails.high.url, utf_data['snippet']['thumbnails']['high']['url'])
        self.assertEqual(data.snippet.thumbnails.high.width, utf_data['snippet']['thumbnails']['high']['width'])
        self.assertEqual(
            data.snippet.thumbnails.high.height, utf_data['snippet']['thumbnails']['high']['height'],
        )

        self.assertEqual(data.snippet.channelTitle, utf_data['snippet']['channelTitle'])
        self.assertEqual(data.snippet.liveBroadcastContent, utf_data['snippet']['liveBroadcastContent'])
