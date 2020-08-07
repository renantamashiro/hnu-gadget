import toga
from toga.style.pack import Pack

from . import hackernews
from newsz.containers import main_block


class Newsz(toga.App):
    def startup(self):
        pass
        # self.main_window = toga.MainWindow(title=self.name, size=(1024, 768))

        # add content to the main window (ex: box, webview, etc)

        # show the main window
        # self.main_window.show()


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
    return toga.App('Hackernews easy', 'renan.tamashiro', startup=build)


def run():
    main().main_loop()
