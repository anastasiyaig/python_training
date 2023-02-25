# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_without_group(app):
    app.contact.add_contact_without_group(Contact(contact_first_name="First name", contact_last_name="Last name"))
