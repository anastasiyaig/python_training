from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(
        contact_first_name="First name updated",
        contact_last_name="Last name updated"))
    app.session.logout()
