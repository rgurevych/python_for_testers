# -*- coding: utf-8 -*-
from models.group import Group
import random

def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
    old_groups = db.get_group_list()
    data_for_edit = Group(name="Edited name", header="Edited header", footer="Edited footer")
    group_for_edit = random.choice(old_groups)
    data_for_edit.id = group_for_edit.id
    app.group.edit_group_by_id(data_for_edit)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group_for_edit)
    old_groups.append(data_for_edit)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.group_id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.group_id_or_max)