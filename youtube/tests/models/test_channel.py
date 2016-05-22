"""
Tests for youtube-api Channel model.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.channel import ChannelListResponse as ChannelResponseParser, Channel as ChannelListItemParser
from youtube.parsers.search import SearchResult
from youtube.models.channel import ChannelsResult as ChannelResultModel, Channel
from youtube.parsers.constants import KIND_CHANNEL


class TestChannelsResult(TestCase):
    """
    Tests for Channel model.
    """

    def setUp(self):
        super(TestChannelsResult, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/channel.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        parsed_data = ChannelResponseParser(self.test_data)
        data = ChannelResultModel.from_channels_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(len(data.channels), len(self.test_data['items']))

        self.assertEqual(data.next_page, self.test_data['nextPageToken'])
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])


class TestChannel(TestCase):
    """
    Tests for Channels model.
    """

    def setUp(self):
        super(TestChannel, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/channel.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        self.test_data = self.test_data['items'][0]
        parsed_data = ChannelListItemParser(self.test_data)
        data = Channel.from_channels_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(data.channel_id, self.test_data['id']['channelId'])
        self.assertEqual(data.id, self.test_data['id']['channelId'])
        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.publish_date, self.test_data['snippet']['publishedAt'])

        self.assertIsNotNone(data.thumbnail)
        self.assertIsNotNone(data.thumbnail.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertIsNotNone(data.thumbnail.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertIsNotNone(data.thumbnail.high, self.test_data['snippet']['thumbnails']['high'])

    def test_model_search_api_data(self):
        test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/search.json"
        ).read()
        test_data = json.loads(test_data_str)

        self.test_data = filter(lambda item: item['id']['kind'] == KIND_CHANNEL, test_data['items'])[0]

        parsed_data = SearchResult(self.test_data)
        data = Channel.from_search_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['id']['kind'])

        self.assertEqual(data.channel_id, self.test_data['id']['channelId'])
        self.assertEqual(data.id, self.test_data['id']['channelId'])
        self.assertEqual(data.title, self.test_data['snippet']['title'])
        self.assertEqual(data.description, self.test_data['snippet']['description'])
        self.assertEqual(data.publish_date, self.test_data['snippet']['publishedAt'])

        self.assertIsNotNone(data.thumbnail)
        self.assertIsNotNone(data.thumbnail.default, self.test_data['snippet']['thumbnails']['default'])
        self.assertIsNotNone(data.thumbnail.medium, self.test_data['snippet']['thumbnails']['medium'])
        self.assertIsNotNone(data.thumbnail.high, self.test_data['snippet']['thumbnails']['high'])
