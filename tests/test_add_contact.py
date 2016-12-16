# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from models.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact("Mister", "Musterman", "+490123456789", "tester@test.com"))
    app.session.logout()

