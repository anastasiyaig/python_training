from model.contact import Contact


def test_edit_contact_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(
        contact_first_name="First name updated"))
    app.session.logout()


def test_edit_contact_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(
        contact_last_name="Last name updated"))
    app.session.logout()
