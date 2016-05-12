__author__ = 'Saleem Latif'


class APIBase(object):
    """
    Base class for all youtube API classes.
    """
    youtube = None

    def __init__(self, youtube):
        self.youtube = youtube

    def fetch(self, **params):
        """
        This method should fetch youtube content, and cache (if used) must only be applied only to this method
        """
        raise NotImplementedError("Subclasses must override this property")

    @property
    def cache_key(self):
        raise NotImplementedError("Subclasses must override this property")
