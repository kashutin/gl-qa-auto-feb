import os

from app.ui.page_objects.login_page import LoginPage
from config.ConfigUI import ConfigUI
from selenium import webdriver



class CosmosIDUI:
    """Class for web app"""

    def __init__(self):
        drv_path = os.getcwd() + r'\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=drv_path)
        self.login_page = LoginPage(self.driver)

    def launch_browser(self):
        """Method for opening browser on the BASE_URL"""
        self.driver.get(url=ConfigUI.BASE_URL)

    def close_browser(self):
        """Method for closing browser"""
        self.driver.quit()
