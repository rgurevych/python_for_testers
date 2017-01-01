# -*- coding: utf-8 -*-

from models.contact import Contact


def test_edit_first_contact_name(app):
    app.contact.edit_first_contact(Contact(first_name="Updated_first_name", last_name="Updated_last_name"))

def test_edit_first_contact_email(app):
    app.contact.edit_first_contact(Contact(email="new_mail@testmail.com"))
