import toga
from toga.style.pack import Pack, COLUMN, RIGHT

from newsz.elements import button


class LeftContainer(toga.Box):
    def __init__(self):
        super().__init__()
        self.style = Pack(
            flex=1,
            direction=COLUMN,
            padding_top=50,
            alignment=RIGHT
        )

    def generate(self, stories):
        for story in stories:
            main_button = button.Article(
                title=f'{story.title}',
                action=story.access_url
            )
            save_button = button.Auxiliary(
                title='Save1',
                action=None
            )
            access_button = button.Auxiliary(
                title='Save2',
                action=None
            )
            children_label = [main_button, save_button, access_button]
            label = button.Label(children_label)
            self.add(label)
