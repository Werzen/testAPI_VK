import requests


class APIClient:
    def __init__(self, url):
        self.url = url

    def __get_requests(self, method, params):
        request = requests.post(f"{self.url}/method/{method}", params=params)
        return request

    def get_users(self, params):
        return self.__get_requests("users.get", params)

    def search_photos(self, params):
        return self.__get_requests("photos.search", params)
