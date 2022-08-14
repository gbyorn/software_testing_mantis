import string
import random
from Model.project import Project


def random_string(max_len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1, max_len))]).rstrip()


def test_create_project(app):
    app.project.open_projects_page()
    old_projects = app.project.get_projects()
    project = Project(project_name=random_string(5), project_description=random_string(10))
    app.project.create_project(project)
    app.project.open_projects_page()
    new_projects = app.project.get_projects()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_create_project_with_soap(app):
    app.project.open_projects_page()
    old_projects = app.soap.get_projects('administrator', 'administrator')
    project = Project(project_name=random_string(5), project_description=random_string(10))
    app.project.create_project(project)
    app.project.open_projects_page()
    new_projects = app.soap.get_projects('administrator', 'administrator')
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
