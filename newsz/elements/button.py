import toga

from toga.style.pack import Pack


class Field(toga.Box):
    def __init__(self, article):
        super().__init__(children=article)
        self.style = Pack(
            padding=6,
        )


class Article(toga.Button):
    def __init__(self, label, action):
        super().__init__(label=label, on_press=action)

        self.label = label
        self.on_press = action
        self.style = Pack(
            width=860,
            height=50
        )


class Auxiliary(toga.Button):
    def __init__(self, label, action):
        super().__init__(label=label, on_press=action)

        self.label = label
        self.on_press = action
        self.style = Pack(
            width=50,
            height=50
        )
