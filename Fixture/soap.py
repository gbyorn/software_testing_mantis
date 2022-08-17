from suds.client import Client
from suds import WebFault
from Model.project import Project


class SoapHelper:

    def __init__(self, app, base_url, soap_credentials):
        self.username = soap_credentials['username']
        self.password = soap_credentials['password']
        self.base_url = base_url
        self.app = app

    def get_projects(self):
        client = Client(f'{self.base_url}api/soap/mantisconnect.php?wsdl')
        try:
            projects = client.service.mc_projects_get_user_accessible(self.username, self.password)
            return [Project(project_id=project.id,
                            project_name=project.name,
                            project_description='') for project in projects]
        except WebFault:
            return []
