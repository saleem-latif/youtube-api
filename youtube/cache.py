__author__ = 'Saleem Latif'

"""
Cache helpers for youtube api helpers
"""
from beaker.cache import cache_managers
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    # Globals
    'cache.regions': 'search, videos, playlists, channels',
    'cache.lock_dir': '/tmp/beaker/lock',
    'cache.data_dir': '/tmp/beaker/data',
    # file region
    'cache.type': 'file',
    'cache.expire': 5 * 24 * 60 * 60,  # 5 day timeout
    }

cache = CacheManager(**parse_cache_config_options(cache_opts))


def get_cache():
    """
    Return a decorator that can be used on a function that needs to be cached

    Returns:
        cache (beaker.cache.CacheManager): cache interface
    """
    return cache


def clear_cache():
    """
    Clear all cache
    """
    for _cache in cache_managers.values():
        _cache.clear()
