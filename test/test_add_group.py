# -*- coding: utf-8 -*-
import pytest
import random
import string

from model.group import Group


def random_string(prefix, maxlen):
    symbols_to_use = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols_to_use) for i in range(random.randrange(maxlen))])


test_data = [Group(group_name="", group_header="", group_footer="")] + \
            [
            Group(
                group_name=random_string("group name", 10),
                group_header=random_string("group header", 20),
                group_footer=random_string("group footer", 20))
            for i in range(5)
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    groups_list_before = app.group.get_group_list()
    group_to_add = group
    app.group.create(group_to_add)
    assert len(groups_list_before) + 1 == app.group.count()
    groups_list_after = app.group.get_group_list()
    groups_list_before.append(group_to_add)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
