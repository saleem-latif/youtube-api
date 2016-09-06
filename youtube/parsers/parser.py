"""
Parsers Base, common parser classes are defined here and used throughout rest of the parsers.
"""
__author__ = 'Saleem Latif'

import json

from youtube.decorators import default_on_error


class ResponseParser(object):
    """
    Base Parser for Youtube data API response.
    """
    def __init__(self, result):
        self.result = result

    @property
    def raw(self):
        return self.result

    @property
    def data(self):
        return JSONParser(self.result).parse()


class ThumbnailsParser(ResponseParser):
    """
    Youtube API parser for thumbnails.
    """
    @property
    @default_on_error((KeyError, TypeError), {})
    def default(self):
        return self.result['default']

    @property
    @default_on_error((KeyError, TypeError), {})
    def medium(self):
        return self.result['medium']

    @property
    @default_on_error((KeyError, TypeError), {})
    def high(self):
        return self.result['high']

    @property
    @default_on_error((KeyError, TypeError), {})
    def maxres(self):
        return self.result['maxres']

    @property
    @default_on_error((KeyError, TypeError), {})
    def standard(self):
        return self.result['standard']


class JSONParser(object):
    """
    json parser that json object, and can be used for attribute access similar to javascript.
    """
    __data__ = {}

    def __init__(self, json_data, *args, **kwargs):
        if isinstance(json_data, dict) or isinstance(json_data, list):
            self.__data__ = json_data
        if isinstance(json_data, basestring):
            self.__data__ = json.loads(json_data, *args, **kwargs)
        elif hasattr(json_data, 'read'):
            self.__data__ = json.load(json_data, *args, **kwargs)

    def parse(self):
        return type("ParserElement", (ParserElement, type(self.__data__)), {"__data__": self.__data__})(self.__data__)


class ParserElement(object):
    """
    JSON Element Parser, attributes are readonly, and attr assignment may give unexpected results.
    """
    __data__ = {}

    def __init__(self, *args, **kwargs):
        super(ParserElement, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        value = self.__data__[item]
        return type("ParserElement", (ParserElement, type(value)), {"__data__": value})(value)

    def __getitem__(self, item):
        value = self.__data__[item]
        return type("ParserElement", (ParserElement, type(value)), {"__data__": value})(value)

    def parse(self, value):
        value_type = type(value)
        return value_type(value)
