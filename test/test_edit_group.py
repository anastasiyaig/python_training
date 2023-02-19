from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(
        group_name="test group updated",
        group_header="test group header updated",
        group_footer="test group footer updated")
    )
    app.session.logout()
