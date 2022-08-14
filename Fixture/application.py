from selenium import webdriver
from selenium.webdriver.common.by import By
from Fixture.session import SessionHelper
from Fixture.project import ProjectHelper


class Application:

    def __init__(self, base_url, browser):
        if browser == "firefox":
            self.webdriver = webdriver.Firefox()
        elif browser == "chrome":
            self.webdriver = webdriver.Chrome()
        elif browser == "ie":
            self.webdriver = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser - {browser}")
        self.session = SessionHelper(self.webdriver)
        self.project = ProjectHelper(self.webdriver)
        self.base_url = base_url

    def open_home_page(self):
        self.webdriver.get(self.base_url)

    def is_valid(self):
        try:
            current_url = self.webdriver.current_url
            return True
        except:
            return False
