import string
import random
from Model.project import Project


def random_string(max_len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))]).rstrip()


def test_delete_project(app):
    if len(app.project.get_projects()) == 0:
        app.project.create_project(Project(project_name='Test', project_description='Test'))
    app.project.open_projects_page()
    old_projects = app.project.get_projects()
    project = random.choice(old_projects)
    app.project.delete_project(project_id=project.project_id)
    app.project.open_projects_page()
    new_projects = app.project.get_projects()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


def test_delete_project_with_soap(app):
    if len(app.soap.get_projects('administrator', 'administrator')) == 0:
        app.project.create_project(Project(project_name='Test', project_description='Test'))
    app.project.open_projects_page()
    old_projects = app.soap.get_projects('administrator', 'administrator')
    project = random.choice(old_projects)
    app.project.delete_project(project_id=project.project_id)
    app.project.open_projects_page()
    new_projects = app.soap.get_projects('administrator', 'administrator')
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
