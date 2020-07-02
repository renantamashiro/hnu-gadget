import unittest
import toga

from newsz import application


class TestApplication(unittest.TestCase):
    def test_app_init(self):
        app_output = application.build(toga.App)
        self.assertIsInstance(app_output, toga.Box)

    def test_main(self):
        self.assertIsInstance(application.main(), toga.App)


