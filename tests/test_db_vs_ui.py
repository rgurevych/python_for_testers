from models.group import Group
from models.contact import Contact

def test_group_list(app, db):
    ui_group_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_group_list = map(clean, db.get_group_list())
    assert sorted(ui_group_list, key = Group.group_id_or_max) == sorted(db_group_list, key = Group.group_id_or_max)


def test_contact_list(app, db):
    ui_contact_list = app.contact.get_contacts_list()
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip())
    db_contact_list = map(clean, db.get_contact_list())
    assert sorted(ui_contact_list, key=Contact.contact_id_or_max) == sorted(db_contact_list, key=Contact.contact_id_or_max)