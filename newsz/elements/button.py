import toga

from toga.style.pack import Pack, CENTER


class Label(toga.Box):
    def __init__(self, article):
        super().__init__(children=article)
        self.style = Pack(
            padding=6,
        )


class Article(toga.Button):
    def __init__(self, title, action):
        super().__init__(label=title, on_press=action)

        self.label = title
        self.on_press = action
        self.style = Pack(
            width=1024,
            height=50
        )


class Auxiliary(toga.Button):
    def __init__(self, title, action):
        super().__init__(label=title, on_press=action)

        self.label = title
        self.on_press = action
        self.style = Pack(
            width=50,
            height=50
        )
