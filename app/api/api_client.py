from app.api.base_requests import BaseRequests
from app.api.urls import Urls
from config.config import Config


class ApiClient(BaseRequests):
    def __init__(self) -> None:
        super().__init__()

    def login(self):
        """Method to execute login"""
        r = self.post(Urls.LOGIN, json=Config.LOGIN_PAYLOAD, headers=Config.LOGIN_HEADER)
        r.raise_for_status()
        token = r.json().get('token')
        if token is None:
            raise Exception("Cannot get token after login")
        self.token = token

    def get_root_folder(self):
        """Method to get root folder"""
        r = self.get(Urls.FILES_V2, headers={"x-token": self.token})
        r.raise_for_status()
        return r.json()

    def get_specific_folder(self, folder_id, item_id):
        """Method to get specific folder"""
        r = self.get(
            Urls.FILES_V2,
            headers={'x-token': self.token},
            params={**Config.ROOT_FOLDER_PARAMS, **{'folder_id': f'{folder_id}', '_': f'{item_id}'}}
        )
        return r.json()

    def get_items_count(self, folder_id, item_id):
        """Method to get count folder"""
        r = self.get(
            Urls.FILES_COUNT_URL,
            headers={'x-token': self.token},
            params={'folder_id': f'{folder_id}', '_': f'{item_id}'}
        )
        return r.json()

    def get_runs(self, folder_id, item_id):
        """Method to get runs requests"""
        r = self.get(
            Urls.FILES_RUN.format(folder_id),
            headers={"x-token": self.token},
            params={'_': f'{item_id}'}
        )
        return r.json()

    def get_analyses(self, folder_id, item_id):
        """Method to get analyses requests"""
        r = self.get(
            Urls.FILES_ANALYSES.format(folder_id),
            headers={'x-token': self.token},
            params={'filter': 'total', '_': f'{item_id}'}
        )
        return r.json()

    def get_artifacts(self, folder_id, item_id):
        """Method to get artifacts requests"""
        r = self.get(
            Urls.FILES_ARTIFACTS.format(folder_id),
            headers={'x-token': self.token},
            params={'_': f'{item_id}'}
        )
        return r.json()
