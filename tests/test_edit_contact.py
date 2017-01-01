# -*- coding: utf-8 -*-

from models.contact import Contact


def test_edit_first_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="Edited_first_name"))
    app.session.logout()

def test_edit_first_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(email="new_mail@testmail.com"))
    app.session.logout()