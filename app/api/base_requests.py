from config.config import Config
import requests
import urllib.parse

class BaseRequests:
    """Class for calling HTTP requests"""

    def __init__(self):
        self.token = None
        self.headers = None

    def form_url(self, url):
        """Method to concat base url and api path"""

        return urllib.parse.urljoin(Config.BASE_URL, url)

    def get(self, path, *args, **kwargs):
        """Reimplementation of GET method"""

        url = self.form_url(path)
        # rest asured
        return requests.get(url, *args, **kwargs)

    def post(self, path, *args, **kwargs):
        """Reimplementation of POST method"""

        url = self.form_url(path)
        # rest asured
        return requests.post(url, *args, **kwargs)