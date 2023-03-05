# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    groups_list_before = app.group.get_group_list()
    app.group.create(Group(
        group_name="test group",
        group_header="test group header",
        group_footer="test group footer"))
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)


def test_add_empty_group(app):
    groups_list_before = app.group.get_group_list()
    app.group.create(Group(
        group_name="",
        group_header="",
        group_footer=""))
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) + 1 == len(groups_list_after)
