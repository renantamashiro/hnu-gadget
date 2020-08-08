import toga
from toga.style.pack import Pack, COLUMN, RIGHT

from . import hackernews
from newsz.elements import button
from newsz.containers import main_block


class Newsz(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(size=(1024, 768), title=self.name)

        self.webview = toga.WebView(url='www.google.com', style=Pack(flex=1))
        self.button_box = toga.Box(
            style=Pack(
                flex=1,
                direction=COLUMN,
                padding_top=50,
                alignment=RIGHT
            )
        )
        self.stories = {}

        self.generate_buttons()

        box = toga.Box(children=[self.button_box, self.webview])

        self.main_window.content = box
        self.main_window.full_screen = True

        self.main_window.show()

    def generate_buttons(self):

        stories = set(hackernews.API.stories(10))
        stories_data = {
            hackernews.Story(hackernews.API.story(i)) for i in stories
        }

        for story in stories_data:
            self.stories[story.title] = story.url
            main_button = button.Article(
                label=story.title,
                action=self.load_page
            )
            save_button = button.Auxiliary(
                label='Save1',
                action=None
            )
            access_button = button.Auxiliary(
                label='Save2',
                action=None
            )
            button_field = button.Field(
                [main_button, save_button, access_button]
            )
            self.button_box.add(button_field)

    # def startup(self):
        # pass
        # self.main_window = toga.MainWindow(title=self.name, size=(1024, 768))

        # add content to the main window (ex: box, webview, etc)

        # show the main window
        # self.main_window.show()

    def load_page(self, widget):
        self.webview.url = self.stories[widget.label]


def build(app):
    right_container = toga.WebView(
        url='https://www.google.com/',
        style=Pack(flex=1))

    stories = set(hackernews.API.stories(10))
    stories_data = {hackernews.Story(hackernews.API.story(i)) for i in stories}

    left_container = main_block.LeftContainer()
    left_container.generate(stories_data)
    box = toga.Box(children=[left_container, right_container])

    return box


def main():
    return Newsz('Hackernews easy', 'renan.tamashiro')


def run():
    main().main_loop()
