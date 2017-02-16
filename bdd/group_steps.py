from pytest_bdd import given, when, then
from models.group import Group
import random

@given('a group list')
def group_list(db):
    return db.get_group_list()

@given('a group with <name>, <header> and <footer>')
def group_for_adding(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, group_for_adding):
    app.group.create(group_for_adding)

@then('the new group list is equal to the old group list with the added group')
def verify_group_added(db, group_list, group_for_adding):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)

@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group_for_deletion"))
    return db.get_group_list()

@given('a random group from the list')
def group_for_deletion(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, group_for_deletion):
    app.group.delete_group_by_id(group_for_deletion.id)

@then('the new group list is equal to the old group list with removed group')
def verify_group_deleted(db, non_empty_group_list, group_for_deletion):
    old_groups=non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(group_for_deletion)
    assert old_groups == new_groups