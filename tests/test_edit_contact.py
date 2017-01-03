# -*- coding: utf-8 -*-

from models.contact import Contact


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    old_contacts = app.contact.get_contacts_list()
    contact_for_editing = Contact(first_name="Updated_first_name", last_name="Updated_last_name")
    contact_for_editing.id = old_contacts[0].id
    app.contact.edit_first_contact(contact_for_editing)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact_for_editing
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)


"""def test_edit_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(email="new_mail@testmail.com"))
    app.open_app_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)"""
