# -*- coding: utf-8 -*-
import pytest
from models.group import Group
import random
import string
import re


def random_string(prefix, max_length):
    sym = string.ascii_letters + string.digits + " "*20
    #The following string generates random string, replaces duplicated spaces with only one and deletes space in the end
    return re.sub('\s+', ' ', (prefix + "".join([random.choice(sym)
                                                 for i in range(random.randrange(max_length))]).rstrip()))


testdata = [Group(name="", header="", footer="")] + [
           Group(name=random_string("name", 10), header=random_string("head", 15), footer=random_string("foot", 15))
           for i in range(5)
           ]


"""testdata = [Group(name=name, header=header, footer=footer)
            for name in ["", random_string("gname", 10)]
            for header in ["", random_string("ghead", 15)]
            for footer in ["", random_string("gfoot", 12)]
    ]"""


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_random_group(app, group):
    old_groups = app.group.get_group_list()
    group_for_adding = group
    app.group.create(group_for_adding)
    assert len(old_groups) == app.group.count() - 1
    new_groups = app.group.get_group_list()
    old_groups.append(group_for_adding)
    assert sorted(old_groups, key=Group.group_id_or_max) == sorted(new_groups, key=Group.group_id_or_max)
