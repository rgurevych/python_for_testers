# -*- coding: utf-8 -*-
from models.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited group name", header="edited header", footer="edited footer"))
    app.session.logout()
