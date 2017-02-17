# -*- coding: utf-8 -*-
from models.contact import Contact
import random
import time
import pytest

def test_delete_any_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.add(Contact(first_name="Contact_for_deletion"))
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact_for_deletion = random.choice(old_contacts)
    with pytest.allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_id(contact_for_deletion.id)
        # time.sleep(5) #for IE only
    with pytest.allure.step('Then the new contact list is equal to the old contact list with removed contact'):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact_for_deletion)
        assert new_contacts == old_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)