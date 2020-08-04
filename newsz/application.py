import toga
from toga.style.pack import Pack, COLUMN, RIGHT

from . import hackernews
from newsz.elements import button


class Newsz(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(1024, 768))

        # add content to the main window (ex: box, webview, etc)

        # show the main window
        self.main_window.show()


def build(app):
    # task: create a class for the right container
    right_container = toga.WebView(
        url='https://www.google.com/',
        style=Pack(flex=1))

    content = toga.Label('Quando o sol se por\
                         nada sobrará além da lua\
                         então não desista fácil assim\
                         do sol')

    # scroll = toga.ScrollContainer(content=content)

    right_container = toga.Box(children=[content])

    # task: create a class for the left container
    left_container = toga.Box(
        style=Pack(flex=1,
                   direction=COLUMN,
                   padding_top=50,
                   alignment=RIGHT
                   ))

    # Right Container contructor
    stories = set(hackernews.API.stories(5))
    stories_data = {hackernews.Story(hackernews.API.story(i)) for i in stories}

    for story in stories_data:
        btn = button.Article(f'{story.title}', action=story.access_url)
        left_container.add(btn)

    box = toga.Box(children=[left_container, right_container])

    return box


def main():
    return toga.App('Hackernews easy', 'renan.tamashiro', startup=build)


def run():
    main().main_loop()
