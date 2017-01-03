# -*- coding: utf-8 -*-
from models.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_deletion"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    app.open_app_page()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts) + 1
