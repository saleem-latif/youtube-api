"""
Tests for youtube-api Videos model.
"""
__author__ = 'Saleem Latif'

import json
from unittest import TestCase
from os import path

from youtube.parsers.videos import VideoListResponse as VideoResponseParser, VideoListItemParser
from youtube.parsers.search import SearchResult
from youtube.models.video import VideosResult as VideoResultModel, Video
from youtube.parsers.constants import KIND_VIDEO


class TestVideosResult(TestCase):
    """
    Tests for Videos model.
    """

    def setUp(self):
        super(TestVideosResult, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/video.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        parsed_data = VideoResponseParser(self.test_data)
        data = VideoResultModel.from_videos_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(len(data.videos), len(self.test_data['items']))

        self.assertEqual(data.next_page, self.test_data['nextPageToken'])
        self.assertEqual(data.total_results, self.test_data['pageInfo']['totalResults'])
        self.assertEqual(data.results_per_page, self.test_data['pageInfo']['resultsPerPage'])


class TestVideo(TestCase):
    """
    Tests for Videos model.
    """

    def setUp(self):
        super(TestVideo, self).setUp()
        self.test_data_str = open(
            path.dirname(path.dirname(__file__)) + "/data/search/video.json"
        ).read()
        self.test_data = json.loads(self.test_data_str)

    def test_model(self):
        self.test_data = self.test_data['items'][0]
        parsed_data = VideoListItemParser(self.test_data)
        data = Video.from_videos_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['kind'])

        self.assertEqual(data.video_id, self.test_data['id']['videoId'])
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
            path.dirname(path.dirname(__file__)) + "/data/search/search.json"
        ).read()
        test_data = json.loads(test_data_str)

        self.test_data = filter(lambda item: item['id']['kind'] == KIND_VIDEO, test_data['items'])[0]

        parsed_data = SearchResult(self.test_data)
        data = Video.from_search_result(parsed_data)

        self.assertEqual(data.etag, self.test_data['etag'])
        self.assertEqual(data.kind, self.test_data['id']['kind'])

        self.assertEqual(data.video_id, self.test_data['id']['videoId'])
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
