# -*- coding: utf-8 -*-
from models.group import Group
import pytest

def test_add_random_group(app, db, json_groups, check_ui):
    group_for_adding = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add the group %s to the list' % group_for_adding):
        app.group.create(group_for_adding)
    with pytest.allure.step('Then the new group list is equal to the old group list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group_for_adding)
        assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.group_id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.group_id_or_max)
