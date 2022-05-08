import pytest
from app.ui.cosmos_id_ui import CosmosIDUI



@pytest.fixture(scope="session")
def ui_app():
    """Fixture for initializing web app instance CosmosIDUI()"""
    # browser = request.config.getoption("browser")????????
    app = CosmosIDUI()
    yield app
    app.driver.quit()

def test_login_failed(ui_app):
    """Test user can't login with wrong credentials"""
    ui_app.login_page.login("svel@suma.com", "nevinosimo")
    assert ui_app.login_page.assert_login_failed()

def test_login_failed2(ui_app):
    """Test user can't login with wrong credentials"""
    ui_app.login_page.login("svel@suma.com", "nevinosimo")
    assert ui_app.login_page.assert_login_failed()
