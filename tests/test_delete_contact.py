# -*- coding: utf-8 -*-
from models.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(first_name="Contact_for_deletion"))
    app.contact.delete_first_contact()
