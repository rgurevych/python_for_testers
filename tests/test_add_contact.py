# -*- coding: utf-8 -*-

from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact_for_adding = Contact(first_name="Mister", last_name="Musterman", mobile_phone="+490123456789", email="tester@test.com")
    app.contact.add(contact_for_adding)
    assert len(old_contacts) == app.contact.count() - 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact_for_adding)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
