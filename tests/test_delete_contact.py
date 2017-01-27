# -*- coding: utf-8 -*-
from models.contact import Contact
import random
import time

def test_delete_any_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Contact_for_deletion"))
    old_contacts = db.get_contact_list()
    contact_for_deletion = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact_for_deletion.id)
    # time.sleep(5) #for IE only
    #assert len(old_contacts) == app.contact.count() + 1
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_for_deletion)
    assert new_contacts == old_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.contact_id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.contact_id_or_max)