# -*- coding: utf-8 -*-

from models.contact import Contact
import random
import pytest

def test_edit_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.add(Contact(first_name="Contact_for_editing"))
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact_for_editing = random.choice(old_contacts)
    with pytest.allure.step('Given a contact data'):
        data_for_editing = Contact(first_name="Updated_first_name", last_name="Updated_last_name")
        data_for_editing.id = contact_for_editing.id
    with pytest.allure.step('When I replace the data in selected contact'):
        app.contact.edit_contact_by_id(data_for_editing)
    with pytest.allure.step(' Then the new contact list is equal to the old contact list with selected contact replaced by a new contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact_for_editing)
        old_contacts.append(data_for_editing)
        assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)