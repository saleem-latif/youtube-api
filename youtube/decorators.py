__author__ = 'Saleem Latif'

from functools import wraps


def default_on_error(error_type, default=None):
    """
    This function returns a decorator that will suppress exceptions of given type
    and returns default value in case of errors.

    Args:
        error_type (Exception subclass):  Exception subclass to suppress
        default : default value to return in case of error
    """
    def __decorator__(func):
        @wraps(func)
        def __decorated__(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_type:
                return default
        return __decorated__
    return __decorator__
