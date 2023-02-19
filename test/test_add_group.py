# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(
        group_name="test group",
        group_header="test group header",
        group_footer="test group footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(
        group_name="",
        group_header="",
        group_footer=""))
    app.session.logout()
