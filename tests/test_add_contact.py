# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    # contact = data_contacts
    old_contacts = db.get_contact_list()
    contact_for_adding = contact
    app.contact.add(contact_for_adding)
    #assert len(old_contacts) == app.contact.count() - 1
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_for_adding)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)