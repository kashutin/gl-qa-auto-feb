from selenium.webdriver.common.by import By
from app.ui.urls import Urls
from app.ui.page_objects.base_page import BasePage

class LoginPage(BasePage):
    """Class defining login page"""

    USERNAME_FIELD = (By.ID, "email")
    PASS_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "signInButton")
    LOGIN_MSG_ERR = (By.ID, "message-id")
    POP_UP_OK_BTN = (By.CSS_SELECTOR, ".css-jckfdu")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        """Perform user login"""
        url = self.form_url(Urls.LOGIN)
        self.driver.get(url)
        self.click(self.POP_UP_OK_BTN)
        self.enter_text(text=username, element=self.USERNAME_FIELD)
        self.enter_text(text=password, element=self.PASS_FIELD)
        self.click(element=self.LOGIN_BTN)

    def assert_login_failed(self):
        """Check incorrect password message pop-up"""
        return self.is_element_present(self.LOGIN_MSG_ERR)

