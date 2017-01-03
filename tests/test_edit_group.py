# -*- coding: utf-8 -*-
from models.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="New edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)