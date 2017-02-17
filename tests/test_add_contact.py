# -*- coding: utf-8 -*-
from models.contact import Contact
import pytest

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a new contact'):
        contact_for_adding = contact
    with pytest.allure.step('When I add the contact to the list'):
        app.contact.add(contact_for_adding)
    with pytest.allure.step('Then the new contact list is equal to the old contact list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact_for_adding)
        assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)