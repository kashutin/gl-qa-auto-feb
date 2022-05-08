import pytest
from app.api.api_client import ApiClient

@pytest.fixture
def apiClient(scope='session'):
    apiClientX = ApiClient()
    apiClientX.login()
    yield apiClientX
    logger.info("test completed")