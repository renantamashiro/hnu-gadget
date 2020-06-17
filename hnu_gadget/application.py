import tkinter as tk

from . import hackernews


def windows_tk(stories):
    window = tk.Tk()

    window.rowconfigure(5, minsize=100, weight=1)
    window.columnconfigure([0], minsize=50, weight=1)
    u = 0
    for i in stories:
        btn = tk.Button(master=window,
                        text=f"{i.title}",
                        command=i.access_url)
        btn.grid(row=u, column=0)
        u += 1

    return window


def run():
    stories = set(hackernews.API.stories(5))
    st = {hackernews.Story(hackernews.API.story(i)) for i in stories}
    window = windows_tk(st)
    window.mainloop()

#    story = hackernews.story(stories[0])
#    title = story['title']
#    url = story['url']
#    click.secho(title, fg="green")
#    click.secho(url)
