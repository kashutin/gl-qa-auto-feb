from app.api.api_client import ApiClient

def test_get_root_folder():
    apiClient = ApiClient()
    apiClient.login()
    rootFolder = apiClient.get_folders()
    assert rootFolder is not None
    print(rootFolder)

test_get_root_folder()