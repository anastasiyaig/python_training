from model.contact import Contact


def test_edit_contact_first_name(app):
    app.contact.edit_first_contact(Contact(
        contact_first_name="First name updated"))


def test_edit_contact_last_name(app):
    app.contact.edit_first_contact(Contact(
        contact_last_name="Last name updated"))
