
import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None

def loadconfig(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as c_file:
            target = json.load(c_file)
    return target

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = loadconfig(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseURL"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def logout_and_destroy():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(logout_and_destroy)
    return fixture


@pytest.fixture(scope = "session")
def db(request):
    db_config = loadconfig(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                          password=db_config["password"])
    def finish():
        dbfixture.destroy()
    request.addfinalizer(finish)
    return dbfixture


@pytest.fixture(scope = "session")
def orm(request):
    orm_config = loadconfig(request.config.getoption("--target"))["db"]
    ormfixture = ORMFixture(host=orm_config["host"], name=orm_config["name"], user=orm_config["user"],
                          password=orm_config["password"])
    return ormfixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f_in:
        return jsonpickle.decode(f_in.read())
