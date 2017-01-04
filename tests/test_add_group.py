# -*- coding: utf-8 -*-

from models.group import Group


def test_add_normal_group(app):
    old_groups = app.group.get_group_list()
    group_for_adding = Group(name="test group 1", header="header 1", footer="footer 1")
    app.group.create(group_for_adding)
    assert len(old_groups) == app.group.count() - 1
    new_groups = app.group.get_group_list()
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)


"""def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group_for_adding = Group(name="", header="", footer="")
    app.group.create(group_for_adding)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) - 1
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)"""
