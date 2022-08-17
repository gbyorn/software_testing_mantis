from selenium import webdriver
from selenium.webdriver.common.by import By
from Fixture.session import SessionHelper
from Fixture.project import ProjectHelper
from Fixture.soap import SoapHelper


class Application:

    def __init__(self, server_url, project_url, browser):
        if browser == "firefox":
            self.webdriver = webdriver.Firefox()
        elif browser == "chrome":
            self.webdriver = webdriver.Chrome()
        elif browser == "ie":
            self.webdriver = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser - {browser}")
        self.server_url = server_url
        self.project_url = project_url
        self.session = SessionHelper(self.webdriver, self.project_url)
        self.project = ProjectHelper(self.webdriver, self.project_url)
        self.soap = SoapHelper(self.webdriver)

    def open_home_page(self):
        self.webdriver.get(self.server_url + self.project_url)

    def is_valid(self):
        try:
            current_url = self.webdriver.current_url
            return True
        except:
            return False
