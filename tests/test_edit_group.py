# -*- coding: utf-8 -*-
from models.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Edited name", header="Edited header", footer="Edited footer"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="New edited footer"))
