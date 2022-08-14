import pytest
import json
import os.path
from Fixture.application import Application


new_app = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as conf_file:
            target = json.load(conf_file)
    return target


@pytest.fixture
def app(request):
    global new_app
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))
    if new_app is None or not new_app.is_valid():
        new_app = Application(browser=browser, base_url=web_config['web']['baseUrl'])
    new_app.open_home_page()
    new_app.session.ensure_login(username=web_config['webadmin']['username'],
                                 password=web_config['webadmin']['password'])
    return new_app


@pytest.fixture(scope='session', autouse=True)
def teardown(request):
    def finalizer():
        new_app.session.ensure_logout()
        new_app.webdriver.quit()
    request.addfinalizer(finalizer)
    return new_app


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
