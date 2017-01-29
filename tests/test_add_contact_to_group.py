from models.group import Group
from models.contact import Contact
import random

def test_add_contact_to_group(app, orm):
    # Check that at least one group exists, create new group if false
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Technical_group"))
    # Select random group for adding contact
    group = random.choice(orm.get_group_list())
    # Check that at least one contact exists, or at least one contact is not in selected group, create new contact if false
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.add(Contact(first_name="Technical_contact"))
    # Select random conact for adding to group
    contact_for_adding = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_to_group(contact_for_adding, group)
    # Check that contact was added to group
    assert contact_for_adding in orm.get_contacts_in_group(group)