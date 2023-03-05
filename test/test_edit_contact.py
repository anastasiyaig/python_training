from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(
        contact_first_name="First name updated"))
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) == len(contacts_list_after)


def test_edit_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    app.contact.edit_first_contact(Contact(
        contact_last_name="Last name updated"))
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) == len(contacts_list_after)
