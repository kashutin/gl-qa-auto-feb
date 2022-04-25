import requests
from app.api.base_requests import BaseRequests
from app.api.urls import Urls
from config.config import Config

class ApiClient(BaseRequests):
    def __init__(self) -> None:
        self.token = None

    def login(self):
        """Method to execute login"""
        r = self.get(Urls.LOGIN, headers=Config.LOGIN_HEADER)
        self.token = r.json().get('token')



    def get_folders(self):
        """Method to get root folder"""
        r = self.get(Urls.ROOT_FOLDER, headers={"x-token": self.token})
        r.raise_for_status()
        return r.json()


