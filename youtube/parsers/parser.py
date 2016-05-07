"""

"""
__author__ = 'Saleem Latif'

import json

from youtube.decorators import default_on_error


class BaseParser(object):
    """

    """
    def __init__(self, result):
        """

        :return:
        """
        self.result = result

    @property
    def raw(self):
        return self.data.id.kind

    @property
    def data(self):
        return JSONParser(self.result).parse()


class ThumbnailsParser(BaseParser):
    """
    Youtube API parser for thumbnails.
    """
    @property
    @default_on_error(KeyError, '')
    def default(self):
        return self.result['default']

    @property
    @default_on_error(KeyError, '')
    def medium(self):
        return self.result['medium']

    @property
    @default_on_error(KeyError, '')
    def high(self):
        return self.result['high']

    @property
    @default_on_error(KeyError, '')
    def maxres(self):
        return self.result['maxres']


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
