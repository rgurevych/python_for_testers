# -*- coding: utf-8 -*-

from models.contact import Contact


def test_add_contact(app):
    app.contact.add(Contact("Mister", "Musterman", "+490123456789", "tester@test.com"))


