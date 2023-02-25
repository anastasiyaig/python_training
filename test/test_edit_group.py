from model.group import Group


def test_edit_group_name(app):
    app.group.edit_first_group(Group(
        group_name="test group name updated"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(
        group_header="test group header updated"))


def test_edit_group_footer(app):
    app.group.edit_first_group(Group(
        group_footer="test group footer updated"))
