from random import randrange

from model.contact import Contact


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    index = randrange(len(contacts_list_before))
    app.contact.delete_contact_by_index(index)
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) - 1 == app.contact.count()
    contacts_list_before[index:index+1] = []
    assert contacts_list_before == contacts_list_after
