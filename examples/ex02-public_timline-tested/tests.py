import unittest
from mock import Mock

import app


class AppTest(unittest.TestCase):

    def test_timeline(self):
        mock = Mock(spec=['get_public_timeline'])
        tl = app.Timeline(impl=mock)
        entries = tl.get_public_entries()
        mock.get_public_timeline.assert_called_with()


class IntegrationTest(unittest.TestCase):

    def test_timeline(self):
        tl = app.Timeline()
        entries = tl.get_public_entries()
        self.assertIsNotNone(entries)
        self.assertTrue(len(entries) > 0)


