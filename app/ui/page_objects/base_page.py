import urllib
from config.ConfigUI import ConfigUI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    ''''Class defines Base Page methods'''

    def __init__(self, driver):
        self.driver = driver

    def form_url(self, url):
        """Join base url and app path"""
        return urllib.parse.urljoin(ConfigUI.BASE_URL, url)

    def enter_text(self, text, element):
        """Enter text into text element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        element.send_keys(text)

    def click(self, element):
        """Click element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        element.click()

    def get_element(self, element):
        """Find element"""
        self.is_element_present(element)
        element = self.driver.find_element(*element)
        return element

    def is_element_present(self, element, timeout=ConfigUI.TIMEOUT):
        """Method-waiter, checking that element is present on the page"""
        try:
            WebDriverWait(self.driver, timeout=timeout).until(
                EC.presence_of_element_located(element)
            )
        except TimeoutException:
            raise TimeoutException(
                f"Cant find element={element} for the timeout={timeout}s"
            )
        return True