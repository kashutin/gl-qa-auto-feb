import requests
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s: %(levelname)s: %(message)s")

login_url = "https://app.cosmosid.com/api/v1/login"
login_payload = {"expiry": 86400, "login_from": "login page"}
login_headers = {"Authorization": "Basic bWFpbGludGVzdEB1a3IubmV0Om1haWxpbnRlc3RAdWtyLm5ldA=="}
rf_url = "https://app.cosmosid.com/api/metagenid/v2/files?"
rf_params = {"breadcrumbs": "1", "offset": "0", "limit": "1000", "folder_id": "84c966d5-8dce-429d-8f92-44d5e28b1581"}


def login():
    r=requests.post(login_url,
                    json=login_payload,
                    headers=login_headers)
    access_token = r.json()['token']
    logging.info(r.raise_for_status)
    return access_token

def root_folder():
    r = requests.get(rf_url, headers={"x-token": a_token}, params=rf_params)
    logging.info(r.json())

a_token = login()
root_folder()
