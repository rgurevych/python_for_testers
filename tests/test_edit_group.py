# -*- coding: utf-8 -*-
from models.group import Group
import random
import pytest

def test_edit_random_group(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Name_for_editing", header="Header_for_editing", footer="Footer_for_editing"))
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a group data'):
        data_for_edit = Group(name="Edited name", header="Edited header", footer="Edited footer")
    with pytest.allure.step('Given a random group from the list'):
        group_for_edit = random.choice(old_groups)
        data_for_edit.id = group_for_edit.id
    with pytest.allure.step('When I replace the data in selected group'):
        app.group.edit_group_by_id(data_for_edit)
    with pytest.allure.step(' Then the new group list is equal to the old group list with selected group replaced by a new group'):
        new_groups = db.get_group_list()
        old_groups.remove(group_for_edit)
        old_groups.append(data_for_edit)
        assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.group_id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.group_id_or_max)