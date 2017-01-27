# -*- coding: utf-8 -*-

from models.contact import Contact
import random


def test_edit_first_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Contact_for_editing"))
    old_contacts = db.get_contact_list()
    contact_for_editing = random.choice(old_contacts)
    data_for_editing = Contact(first_name="Updated_first_name", last_name="Updated_last_name")
    data_for_editing.id = contact_for_editing.id
    app.contact.edit_contact_by_id(data_for_editing)
    #assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_for_editing)
    old_contacts.append(data_for_editing)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)