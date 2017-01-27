# -*- coding: utf-8 -*-
from models.group import Group
import random

def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group_for_deletion"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    #assert len(old_groups) == app.group.count() + 1
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.group_id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.group_id_or_max)
