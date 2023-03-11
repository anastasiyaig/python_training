# -*- coding: utf-8 -*-
import random
import string

import pytest

from model.contact import Contact


def random_string(prefix, maxlen):
    symbols_to_use = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols_to_use) for i in range(random.randrange(maxlen))])


test_data = [Contact(contact_first_name="", contact_last_name="")] + \
            [
                Contact(
                    contact_first_name=random_string("first name", 15),
                    contact_last_name=random_string("last name", 30))
                for i in range(5)
            ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact_without_group(app, contact):
    contacts_list_before = app.contact.get_contacts_list()
    contact_to_add = contact
    app.contact.add_contact_without_group(contact_to_add)
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) + 1 == app.contact.count()
    contacts_list_before.append(contact_to_add)
    assert sorted(contacts_list_before, key=Contact.id_or_max) == sorted(contacts_list_after, key=Contact.id_or_max)
