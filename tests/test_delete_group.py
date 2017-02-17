# -*- coding: utf-8 -*-
from models.group import Group
import random
import pytest

def test_delete_random_group(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Group_for_deletion"))
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with pytest.allure.step('When I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old group list with removed group'):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(new_groups, key=Group.group_id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.group_id_or_max)
