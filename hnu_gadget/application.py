import toga

from . import hackernews


def build(app):
    box = toga.Box()

    stories = set(hackernews.API.stories(5))
    st = {hackernews.Story(hackernews.API.story(i)) for i in stories}

    for i in st:
        btn = toga.Button(f'{i.title}', on_press=i.access_url)
        box.add(btn)

    return box


def main():
    return toga.App('Hackernews easy', 'renan.tamashiro', startup=build)


def run():
    main().main_loop()
