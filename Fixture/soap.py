from suds.client import Client
from suds import WebFault
from Model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects(self, username, password):
        client = Client('http://localhost:8080/mantisbt-2.25.5/api/soap/mantisconnect.php?wsdl')
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            return [Project(project_id=project.id,
                            project_name=project.name,
                            project_description='') for project in projects]
        except WebFault:
            return []
