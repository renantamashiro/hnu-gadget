import unittest

from newsz import application


class TestApplication(unittest.TestCase):
    def test_main(self):
        self.assertIsInstance(application.main(), application.Newsz)
