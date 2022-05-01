import pytest
from app.api.api_client import ApiClient
import logging

logger = logging.getLogger()

@pytest.fixture
def apiClient(scope='session'):
    apiClientX = ApiClient()
    apiClientX.login()
    yield apiClientX
    logger.info("test completed")

def test_login_succesfull(apiClient):
    print(apiClient.token)
    assert apiClient.token is not None

def test_get_root_folder(apiClient):
    rootFolder = apiClient.get_root_folder()
    print(rootFolder)
    assert rootFolder is not None

def test_get_specific_folder(apiClient):
    specificFolder = apiClient.get_specific_folder('84c966d5-8dce-429d-8f92-44d5e28b1581', '1622700773180')
    print(specificFolder)
    assert specificFolder is not None

def test_get_items_count(apiClient):
    itemsCount = apiClient.get_items_count('84c966d5-8dce-429d-8f92-44d5e28b1581', '1622700773179')
    print(itemsCount)
    assert itemsCount is not None

def test_get_runs(apiClient):
    runCount = apiClient.get_runs('7f4c7326-0a4e-4b56-a8d0-8ce002191672', '1622700773181')
    print(runCount)
    assert runCount is not None

def test_get_analyses(apiClient):
    analyses = apiClient.get_analyses('437ef8e4-b595-4fd8-a2f5-64221831e925', '1622700773184')
    print(analyses)
    assert analyses is not None

def test_get_artifacts(apiClient):
    atrifacts = apiClient.get_artifacts('437ef8e4-b595-4fd8-a2f5-64221831e925', '1622700773185')
    print(atrifacts)
    assert atrifacts is not None

# def test_test(apiClient):
#     r = apiClient.get("https://app.cosmosid.com/api/metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/analysis?filter=total&_=1622700773184")
#     print(r.json())

# test_login_succesfull()
# test_get_root_folder()
