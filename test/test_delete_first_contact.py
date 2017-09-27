# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(Contact(firstname="New contact to delete"))
    app.contact.delete_first_contact()
