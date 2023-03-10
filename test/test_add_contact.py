# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_without_group(app):
    contacts_list_before = app.contact.get_contacts_list()
    contact_to_add = Contact(contact_first_name="First name", contact_last_name="Last name")
    app.contact.add_contact_without_group(contact_to_add)
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) + 1 == app.contact.count()
    contacts_list_before.append(contact_to_add)
    assert sorted(contacts_list_before, key=Contact.id_or_max) == sorted(contacts_list_after, key=Contact.id_or_max)


