import toga

from toga.style.pack import Pack


class Article(toga.Button):
    def __init__(self, title, action):
        super().__init__(label=title, on_press=action)

        self.label = title
        self.on_press = action
        self.style = Pack(
            padding_top=40,
            padding_bottom=40
        )
