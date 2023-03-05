from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    group_to_edit = Group(
        group_name="test group name updated")
    group_to_edit.group_id = groups_list_before[0].group_id
    app.group.edit_first_group(group_to_edit)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == app.group.count()
    groups_list_before[0] = group_to_edit
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    group_to_edit = Group(
        group_header="test group header updated")
    group_to_edit.group_id = groups_list_before[0].group_id
    app.group.edit_first_group(group_to_edit)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == app.group.count()
    groups_list_before[0] = group_to_edit
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    group_to_edit = Group(
        group_footer="test group footer updated")
    group_to_edit.group_id = groups_list_before[0].group_id
    app.group.edit_first_group(group_to_edit)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) == app.group.count()
    groups_list_before[0] = group_to_edit
    assert sorted(groups_list_before, key=Group.id_or_max) == sorted(groups_list_after, key=Group.id_or_max)
