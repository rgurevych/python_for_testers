# -*- coding: utf-8 -*-
import pytest
from models.group import Group
from data.groups import testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_random_group(app, group):
    old_groups = app.group.get_group_list()
    group_for_adding = group
    app.group.create(group_for_adding)
    assert len(old_groups) == app.group.count() - 1
    new_groups = app.group.get_group_list()
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
