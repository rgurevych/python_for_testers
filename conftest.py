
import pytest
import json
import os.path
from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as c_file:
            target = json.load(c_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseURL"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def logout_and_destroy():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(logout_and_destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", default="target.json")