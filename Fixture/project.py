from Model.project import Project
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver


class ProjectHelper:

    def __init__(self, app: WebDriver):
        self.app = app
        self.project_cache = None

    def create_project(self, project: Project):
        self.open_projects_page()
        self.app.find_element(By.XPATH, "//button[@type='submit']").click()
        self.write_data(project.project_name, project.project_description)
        self.app.find_element(By.XPATH, "//input[@type='submit']").click()
        self.open_projects_page()

    def open_projects_page(self):
        if not (self.app.current_url.endswith("manage_proj_page.php")):
            self.app.find_element(By.XPATH, "//li/a[@href='/mantisbt-2.25.5/manage_overview_page.php']").click()
            self.app.find_element(By.XPATH, "//li/a[@href='/mantisbt-2.25.5/manage_proj_page.php']").click()

    def write_data(self, name: str | None = None, description: str | None = None):
        self.app.find_element(By.NAME, "name").click()
        self.app.find_element(By.NAME, "name").clear()
        self.app.find_element(By.NAME, "name").send_keys(name)
        self.app.find_element(By.NAME, "description").click()
        self.app.find_element(By.NAME, "description").clear()
        self.app.find_element(By.NAME, "description").send_keys(description)

    def get_projects(self):
        self.open_projects_page()
        project_list = []
        for project in self.app.find_elements(By.XPATH, "//div[@class='table-responsive']/table/tbody/tr/td/a"):
            project_id = project.get_attribute('href').split('=')[1]
            project_name = project.get_attribute('text')
            project_list.append(Project(project_name=project_name, project_id=project_id, project_description=''))
        return project_list

    def delete_project(self, project_id):
        self.open_projects_page()
        self.app.find_element(By.XPATH, f"//tbody/tr/td/a[@href='manage_proj_edit_page.php?project_id={project_id}']").click()
        self.app.find_element(By.XPATH, "//input[@value=\"Удалить проект\"]").click()
        self.app.find_element(By.XPATH, "//input[@value=\"Удалить проект\"]").click()
