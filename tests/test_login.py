from app.api.api_client import ApiClient


apiClient = ApiClient()
apiClient.login()

def test_login_succesfull():
    assert apiClient.token is not None
    print(apiClient.token)

def test_get_root_folder():
    rootFolder = apiClient.get_folders()
    assert rootFolder is not None
    print(rootFolder)

test_login_succesfull()
test_get_root_folder()

