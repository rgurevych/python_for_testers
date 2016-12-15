# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact("Mister", "Musterman", "+490123456789", "tester@test.com"))
    app.logout()

