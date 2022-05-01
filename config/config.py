import base64
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Class defines all the configuration for test framework"""

    BASE_URL = "http://app.cosmosid.com"
    CREDENTIALS = os.getenv('CREDENTIALS', None)
    LOGIN_HEADER = {"Authorization": f"Basic {CREDENTIALS}"}
    LOGIN_PAYLOAD = {"expiry": 86400, "login_from": "login page"}
    ROOT_FOLDER_PARAMS = {"breadcrumbs": "1", "offset": "0", "limit": "1000"}

