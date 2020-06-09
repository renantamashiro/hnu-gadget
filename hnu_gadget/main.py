import requests
import click


def main():
    stories = get_stories()
    story = get_story(stories[0])
    title = story['title']
    url = story['url']
    click.secho(title, fg="green")
    click.secho(url)


def get_stories():
    API_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()
    return data


def get_story(id_story):
    API_URL = f'https://hacker-news.firebaseio.com/v0/item/{id_story}.json?print=pretty'

    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()

    return data

