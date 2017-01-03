# -*- coding: utf-8 -*-

from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(Contact(first_name="Mister", last_name="Musterman", mobile_phone="+490123456789", email="tester@test.com"))
    app.open_app_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts) - 1
