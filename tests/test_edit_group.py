# -*- coding: utf-8 -*-
from models.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    group_for_editing = Group(name="Edited name", header="Edited header", footer="Edited footer")
    group_for_editing.id = old_groups[0].id
    app.group.edit_first_group(group_for_editing)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group_for_editing
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


"""def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="New edited footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)"""