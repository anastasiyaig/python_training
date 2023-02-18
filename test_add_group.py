# -*- coding: utf-8 -*-
import pytest

from application import Application
from group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_group(Group(
        group_name="test group",
        group_header="test group header",
        group_footer="test group footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(
        group_name="",
        group_header="",
        group_footer=""))
    app.logout()
