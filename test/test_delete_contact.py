from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) - 1 == len(contacts_list_after)
    contacts_list_before[0:1] = []
    assert contacts_list_before == contacts_list_after
