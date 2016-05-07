__author__ = 'Saleem Latif'


class APIBase(object):
    """

    """
    youtube = None

    def __init__(self, youtube):
        self.youtube = youtube

    @property
    def cache_key(self):
        raise NotImplementedError("Subclasses must override this property")
