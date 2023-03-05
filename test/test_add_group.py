# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    groups_list_before = app.group.get_group_list()
    group_to_add = Group(
        group_name="test group",
        group_header="test group header",
        group_footer="test group footer")
    app.group.create(group_to_add)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group_to_add)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)


def test_add_empty_group(app):
    groups_list_before = app.group.get_group_list()
    group_to_add = Group(
        group_name="test group",
        group_header="test group header",
        group_footer="test group footer")
    app.group.create(group_to_add)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
    groups_list_before.append(group_to_add)
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
