"""
Test for decorators.
"""
from unittest import TestCase
from youtube.decorators import default_on_error


class DecoratorTest(TestCase):
    """
    Tests for decorators
    """
    def test_default_on_error(self):
        test_dict = {
            "key1": {
                "key1.1": "value"
            },
            "key2": [],
        }

        # Make sure key error is raised if key does not exists
        with self.assertRaises(KeyError):
            value = test_dict["key1"]["dummy"]

        @default_on_error(KeyError, 'default')
        def value():
            return test_dict["key1"]["dummy"]

        # Make sure default is returned if key does not exist
        self.assertEqual(value(), "default")

        # Make sure multiple exceptions can be caught
        @default_on_error((KeyError, TypeError), 'default')
        def value():
            return test_dict["key2"]["dummy"]

        # Make sure default is returned if key does not exist
        self.assertEqual(value(), "default")
