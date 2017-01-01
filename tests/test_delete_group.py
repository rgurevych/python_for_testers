# -*- coding: utf-8 -*-
from models.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_for_deletion"))
    app.group.delete_first_group()
