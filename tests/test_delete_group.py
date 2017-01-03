# -*- coding: utf-8 -*-
from models.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group_for_deletion"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) + 1
