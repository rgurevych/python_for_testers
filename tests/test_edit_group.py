# -*- coding: utf-8 -*-
from models.group import Group
from random import randrange

def test_edit_any_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    group_for_editing = Group(name="Edited name", header="Edited header", footer="Edited footer")
    index = randrange(len(old_groups))
    group_for_editing.id = old_groups[index].id
    app.group.edit_any_group(group_for_editing, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group_for_editing
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


"""def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="New edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""