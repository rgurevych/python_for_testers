# -*- coding: utf-8 -*-

from models.contact import Contact


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact("Mister", "Musterman", "+490123456789", "tester@test.com"))
    app.session.logout()

