from sys import maxsize


class Project:
    def __init__(self, project_name: str | None = None, project_description: str | None = None, project_id=None):
        self.project_name = project_name
        self.project_description = project_description
        self.project_id = project_id

    def __repr__(self):
        return f'{self.project_id}:{self.project_name}'

    def __eq__(self, other):
        return (self.project_id == other.project_id or self.project_id is None or other.project_id is None) \
               and self.project_name == other.project_name

    def id_or_max(self):
        return int(self.project_id) if self.project_id else maxsize
