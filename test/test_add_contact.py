# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_without_group(app):
    contacts_list_before = app.contact.get_contacts_list()
    app.contact.add_contact_without_group(Contact(contact_first_name="First name", contact_last_name="Last name"))
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) + 1 == len(contacts_list_after)
