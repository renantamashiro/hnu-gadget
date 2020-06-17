import requests
import webbrowser


class Story:
    def __init__(self, data):
        self.title = data['title']
        self.url = data['url']

    def access_url(self):
        webbrowser.open(self.url, autoraise=True)


class API:

    @classmethod
    def stories(self, number):
        API_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()
        return data[:number]

    @classmethod
    def story(self, id_story):
        API_URL = f'https://hacker-news.firebaseio.com/v0/item/{id_story}.json?print=pretty'

        with requests.get(API_URL) as response:
            response.raise_for_status()
            data = response.json()
        return data

