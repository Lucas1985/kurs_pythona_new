# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Contact(firstname="New contact to modify"))
    app.contact.modify_first_contact(Contact(firstname="New name"))


def test_modify_first_contact_surename(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Contact(firstname="New contact to modify"))
    app.contact.modify_first_contact(Contact(surename="New surename"))