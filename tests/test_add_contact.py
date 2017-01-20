# -*- coding: utf-8 -*-
import pytest
from models.contact import Contact
from data.add_contact import testdata


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    contact_for_adding = contact
    app.contact.add(contact_for_adding)
    assert len(old_contacts) == app.contact.count() - 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact_for_adding)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
