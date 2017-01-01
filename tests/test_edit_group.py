# -*- coding: utf-8 -*-
from models.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    app.session.logout()

def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="New edited footer"))
    app.session.logout()