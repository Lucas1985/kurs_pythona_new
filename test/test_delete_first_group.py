# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group.count_of_groups() == 0:
        app.group.create(Group(name="New group to delete"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)