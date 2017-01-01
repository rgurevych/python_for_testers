# -*- coding: utf-8 -*-

from models.contact import Contact


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    app.contact.edit_first_contact(Contact(first_name="Updated_first_name", last_name="Updated_last_name"))

def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    app.contact.edit_first_contact(Contact(email="new_mail@testmail.com"))
