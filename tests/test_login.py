import pytest
from app.api.api_client import ApiClient
import logging

# logger = logging.getLogger()
class ConsLogger:
    def info(self, msg):
        print(msg)
logger = ConsLogger()

@pytest.fixture
def apiClient(scope='session'):
    apiClientX = ApiClient()
    apiClientX.login()
    yield apiClientX
    logger.info("test completed")

def test_login_succesfull(apiClient):
    logger.info(apiClient.token)
    assert apiClient.token is not None

def test_get_root_folder(apiClient):
    rootFolder = apiClient.get_root_folder()
    logger.info(rootFolder)
    assert rootFolder['items'][0]['name'] == 'CID1_LC3.fasta'

def test_get_specific_folder(apiClient):
    specificFolder = apiClient.get_specific_folder('84c966d5-8dce-429d-8f92-44d5e28b1581', '1622700773180')
    logger.info(specificFolder)
    assert specificFolder['items'][0]['name'] == 'Amplicon_Examples'

def test_get_items_count(apiClient):
    itemsCount = apiClient.get_items_count('84c966d5-8dce-429d-8f92-44d5e28b1581', '1622700773179')
    logger.info(itemsCount)
    assert itemsCount['total'] == 59

def test_get_runs(apiClient):
    runCount = apiClient.get_runs('7f4c7326-0a4e-4b56-a8d0-8ce002191672', '1622700773181')
    logger.info("Runs Count is: " + str(len(runCount['runs'])))
    assert len(runCount['runs']) > 0

def test_get_analyses(apiClient):
    analysis = apiClient.get_analysis('437ef8e4-b595-4fd8-a2f5-64221831e925', '1622700773184')
    logger.info(analysis)
    assert analysis['analysis'][0]['status'] == 'Success'

def test_get_artifacts(apiClient):
    atrifacts = apiClient.get_artifacts('437ef8e4-b595-4fd8-a2f5-64221831e925', '1622700773185')
    logger.info(atrifacts)
    assert atrifacts['artifacts'][0]['status'] == 'Success'
