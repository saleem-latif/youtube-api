__author__ = 'Saleem Latif'

from datetime import datetime, timedelta
import pytz

from youtube.api import Youtube as YoutubeBase


class YoutubeAPIShortcutsMixin(object):
    """
    Add this Mixin to Youtube API base class to get short functions defined here.
    """
    def fetch_video(self, video_id):
        """
        Fetch Video resource, return None if it could not be found.
        Args:
            video_id (str): Youtube video id for the given video
        Returns:
            video (youtube.parsers.videos.VideoListItemParser): Fetched Video resource or None
        """
        result = self.videos(id=video_id)
        return result.items[0] if len(result.items) > 0 else None

    def fetch_videos(self, video_ids):
        """
        Fetch Video resources.

        Args:
            video_ids (list): list of Youtube video ids.
        Returns:
            video (youtube.parsers.videos.VideoListResponse): Fetched Video resource or None
        """
        result = self.videos(id=", ".join(video_ids))
        return result

    def fetch_channel_videos(self, channel_id, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='video',
            order='viewCount',
            channelId=channel_id,
            **kwargs
        )
        return result

    def fetch_playlist_videos(self, playlist_id, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.playlists(
            playlistId=playlist_id,
            **kwargs
        )
        return result

    def fetch_most_viewed_videos(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='video',
            order='viewCount',
            **kwargs
        )
        return result

    def fetch_related_videos(self, video_id, page=None):
        kwargs = {}
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='video',
            order='viewCount',
            relatedToVideoId=video_id,
            **kwargs
        )
        return result

    def fetch_top_recent_videos(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        publish_date = pytz.UTC.localize(datetime.now() - timedelta(days=45))
        result = self.search(
            q='',
            type='video',
            order='viewCount',
            publishedAfter=publish_date.isoformat(),
            **kwargs
        )
        return result

    def fetch_top_rated_videos(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='video',
            order='rating',
            **kwargs
        )
        return result

    def fetch_most_recent_videos(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='video',
            order='date',
            **kwargs
        )
        return result

    def fetch_most_viewed_channels(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='channel',
            order='viewCount',
            **kwargs
        )
        return result

    def fetch_most_liked_channels(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='channel',
            order='rating',
            **kwargs
        )
        return result

    def fetch_top_recent_channels(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='channel',
            order='rating',
            **kwargs
        )
        return result

    def fetch_most_recent_channels(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='channel',
            order='date',
            **kwargs
        )
        return result

    def fetch_most_viewed_play_lists(self, category=0, page=None):
        kwargs = {}
        if category:
            kwargs.update({
                'videoCategoryId': category,
            })
        if page:
            kwargs.update({
                "pageToken": page
            })

        result = self.search(
            q='',
            type='playlist',
            order='viewCount',
            **kwargs
        )
        return result


class Youtube(YoutubeBase, YoutubeAPIShortcutsMixin):
    pass
