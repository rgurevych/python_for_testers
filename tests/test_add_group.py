# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from models.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_normal_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test group 1", header="header 1", footer="footer 1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
