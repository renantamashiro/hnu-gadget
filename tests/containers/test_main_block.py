import unittest
import toga

from newsz.containers import main_block
from newsz.hackernews import Story
from newsz.elements import button


class MainBlockTests(unittest.TestCase):
    def setUp(self):
        self.left_container = main_block.LeftContainer()

    def test_instance_left_container(self):
        self.assertIsInstance(self.left_container, toga.Box)

    def test_left_container_generate(self):
        stories = {
            'title': 'spyman',
            'url': 'www.renan.com',
            'content': 'Test content'
        }

        stories_test = {Story(stories)}

        self.left_container.generate(stories_test)

        label_title = self.left_container.children[0].children[0].label

        self.assertEqual(label_title, stories['title'])
        self.assertIsInstance(self.left_container.children[0], button.Label)
