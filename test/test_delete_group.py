from random import randrange

from model.group import Group


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="created as precondition"))
    groups_list_before = app.group.get_group_list()
    index = randrange(len(groups_list_before))
    app.group.delete_group_by_index(index)
    groups_list_after = app.group.get_group_list()
    assert len(groups_list_before) - 1 == app.group.count()
    groups_list_before[index:index + 1] = []
    assert groups_list_before == groups_list_after
