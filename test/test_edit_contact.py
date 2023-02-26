from model.contact import Contact


def test_edit_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    app.contact.edit_first_contact(Contact(
        contact_first_name="First name updated"))


def test_edit_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.add_contact_without_group(Contact(contact_first_name="contact as precondition"))
    app.contact.edit_first_contact(Contact(
        contact_last_name="Last name updated"))
