from models.group import Group
from models.contact import Contact
import random

def test_delete_contact_from_group(app, orm):
    # Check that at least one group exists, create new group if false
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Technical_group"))
    # Select random group
    group = random.choice(orm.get_group_list())
    # Check that at least one contact exists, create new contact if false
    if len(orm.get_contact_list()) == 0:
        app.contact.add(Contact(first_name="Technical_contact"))
    # Check that selected group contains at least one contact, add one if false
    if len(orm.get_contacts_in_group(group)) == 0:
        contact_for_adding = random.choice(orm.get_contacts_not_in_group(group))
        app.contact.add_contact_to_group(contact_for_adding, group)
        # Check that contact was actually added to group
        assert contact_for_adding in orm.get_contacts_in_group(group)
    # Select random contact for deletion
    contact_for_deletion = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_contact_from_group(contact_for_deletion, group)
    # Check that contact was actually deleted from group
    assert contact_for_deletion not in orm.get_contacts_in_group(group)
    # Check that contact was not deleted completely, just removed from group
    assert contact_for_deletion in orm.get_contacts_not_in_group(group)
