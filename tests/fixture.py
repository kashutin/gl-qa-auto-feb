import pytest
from app.api.api_client import ApiClient

@pytest.fixture
def apiClient():
    apiClientX = ApiClient()
    apiClientX.login()
    return apiClientX