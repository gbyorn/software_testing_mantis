from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class SessionHelper:

    def __init__(self, app: WebDriver):
        self.app = app

    def login(self, username: str, password: str):
        self.app.find_element(By.NAME, "username").click()
        self.app.find_element(By.NAME, "username").clear()
        self.app.find_element(By.NAME, "username").send_keys(username)
        self.app.find_element(By.XPATH, "//input[@value='Вход']").click()
        self.app.find_element(By.NAME, "password").click()
        self.app.find_element(By.NAME, "password").clear()
        self.app.find_element(By.NAME, "password").send_keys(password)
        self.app.find_element(By.XPATH, "//input[@value='Вход']").click()

    def logout(self):
        self.app.find_element(By.XPATH, "//li/a[@href='/mantisbt-2.25.5/logout_page.php']")

    def ensure_login(self, username: str, password: str):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        return len(self.app.find_elements(By.XPATH, "//span[@class='user-info']")) > 0

    def is_logged_in_as(self, username: str):
        return self.app.find_element(By.XPATH, "//span[@class='user-info']").text == username
