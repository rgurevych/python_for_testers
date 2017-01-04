# -*- coding: utf-8 -*-
from models.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_deletion"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts) == app.contact.count() + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0:1] = []
    assert new_contacts == old_contacts
