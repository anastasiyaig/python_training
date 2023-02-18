# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact_without_group(app):
    app.login(username="admin", password="secret")
    app.add_contact_without_group(Contact(contact_first_name="First name", contact_last_name="Last name"))
    app.logout()
