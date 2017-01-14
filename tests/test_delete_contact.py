# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange
import time

def test_delete_any_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_deletion"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_any_contact(index)
    #time.sleep(5)
    assert len(old_contacts) == app.contact.count() + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts
