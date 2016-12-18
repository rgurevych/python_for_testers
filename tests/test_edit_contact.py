# -*- coding: utf-8 -*-
from models.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("Edited_first_name", "Edited_last_name", "+49555555555", "edited_mail@test.com"))
    app.session.logout()