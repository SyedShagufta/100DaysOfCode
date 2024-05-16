import requests


class Post:
    def __init__(self):
        self.END_POINT = "https://api.npoint.io/7009cb18e5cc9c2fd534"
        self.response = (requests.get(self.END_POINT)).json()

    def get_posts(self):
        return self.response
