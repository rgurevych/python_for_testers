# -*- coding: utf-8 -*-
from models.group import Group

def test_add_random_group(app, db, json_groups):
    # group = data_groups
    group_for_adding = json_groups
    old_groups = db.get_group_list()
    app.group.create(group_for_adding)
    #assert len(old_groups) == app.group.count() - 1
    new_groups = db.get_group_list()
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
