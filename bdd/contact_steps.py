from pytest_bdd import given, when, then
from models.contact import Contact
from data.contacts import testdata
import random

@given('a contact list')
def contact_list(db):
    return db.get_contact_list()

@given('a new contact')
def contact_for_adding():
    return testdata[0]

@when('I add the contact to the list')
def add_new_contact(app, contact_for_adding):
    app.contact.add(contact_for_adding)

@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, contact_for_adding):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_for_adding)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)

@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Technical_contact"))
    return db.get_contact_list()

@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)

@then('the new contact list is equal to the old contact list with removed contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts=non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert new_contacts == old_contacts

@given('a contact data containing <firstname> and <lastname>')
def data_for_editing(firstname, lastname, random_contact):
    return Contact(first_name=firstname, last_name=lastname, id=random_contact.id)

@when('I replace the data in selected contact')
def edit_contact(app, data_for_editing):
    app.contact.edit_contact_by_id(data_for_editing)

@then('the new contact list is equal to the old contact list with selected contact replaced by a new contact')
def verify_contact_edited(db, non_empty_contact_list, random_contact, data_for_editing):
    old_contacts=non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(data_for_editing)
    assert sorted(old_contacts, key=Contact.contact_id_or_max) == sorted(new_contacts, key=Contact.contact_id_or_max)