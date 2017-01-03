# -*- coding: utf-8 -*-

from models.group import Group


def test_add_normal_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test group 1", header="header 1", footer="footer 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) - 1


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups) - 1

