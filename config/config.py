import os

class Config:
    """Class defines all the configuration for test framework"""

    BASE_URL = "http://app.cosmosid.com"
    LOGIN_TOKEN = os.environ.get('LOGIN_TOKEN', None)
    LOGIN_PAYLOAD = {"expiry": 86400, "login_from": "login page"}
    LOGIN_HEADER = {"Authorization": "Basic bWFpbGludGVzdEB1a3IubmV0Om1haWxpbnRlc3RAdWtyLm5ldA=="}
    ROOT_FOLDER_PARAMS = {"breadcrumbs": "1", "offset": "0", "limit": "1000",
                 "folder_id": "84c966d5-8dce-429d-8f92-44d5e28b1581"}


