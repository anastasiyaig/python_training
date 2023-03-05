from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    app.group.edit_first_group(Group(
        group_name="test group name updated"))
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    app.group.edit_first_group(Group(
        group_header="test group header updated"))
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    app.group.edit_first_group(Group(
        group_footer="test group footer updated"))
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == len(groups_list_after)
