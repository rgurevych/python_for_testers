# -*- coding: utf-8 -*-

from models.group import Group


def test_add_normal_group(app):
    app.group.create(Group(name="test group 1", header="header 1", footer="footer 1"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

