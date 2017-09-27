# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(firstname="Łukasz", surename="Bartyzel", address="Warszawska"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", surename="", address=""))



