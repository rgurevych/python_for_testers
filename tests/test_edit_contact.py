# -*- coding: utf-8 -*-

from models.contact import Contact


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(first_name="Updated_first_name", last_name="Updated_last_name"))
    app.open_app_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(email="new_mail@testmail.com"))
    app.open_app_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
