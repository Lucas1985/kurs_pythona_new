# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count_of_groups() == 0:
        app.group.create(Group(name="New group to modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="New group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count_of_groups() == 0:
        app.group.create(Group(name="New group to modify"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

