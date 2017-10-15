# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact_name(app):
    contact = Contact(firstname="New name", surename="New surename")
    if app.contact.count_of_contact() == 0:
        app.contact.create_contact(contact)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.contact_id = old_contacts[index].contact_id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_first_contact_surename(app):
#    if app.contact.count_of_contact() == 0:
#        app.contact.create_contact(Contact(firstname="New contact to modify"))
#    app.contact.modify_first_contact(Contact(surename="New surename"))