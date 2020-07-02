import toga
from toga.style.pack import Pack, COLUMN, RIGHT

from . import hackernews


def build(app):
    # task: create a class for the right container
    right_container = toga.WebView(
        url='https://www.google.com/',
        style=Pack(flex=1))

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
        btn = toga.Button(f'{story.title}', on_press=story.access_url)
        left_container.add(btn)

    box = toga.Box(children=[left_container, right_container])

    return box


def main():
    return toga.App('Hackernews easy', 'renan.tamashiro', startup=build)


def run():
    main().main_loop()
