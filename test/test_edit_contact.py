from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    contact_to_edit = Contact(contact_first_name="First name updated")
    contact_to_edit.contact_id = contacts_list_before[0].contact_id
    app.contact.edit_first_contact(contact_to_edit)
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) == app.contact.count()
    contacts_list_before[0] = contact_to_edit
    assert sorted(contacts_list_before, key=Contact.id_or_max) == sorted(contacts_list_after, key=Contact.id_or_max)


def test_edit_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    contacts_list_before = app.contact.get_contacts_list()
    contact_to_edit = Contact(contact_last_name="Last name updated")
    contact_to_edit.contact_id = contacts_list_before[0].contact_id
    app.contact.edit_first_contact(contact_to_edit)
    contacts_list_after = app.contact.get_contacts_list()
    assert len(contacts_list_before) == app.contact.count()
    contacts_list_before[0] = contact_to_edit
    assert sorted(contacts_list_before, key=Contact.id_or_max) == sorted(contacts_list_after, key=Contact.id_or_max)
