import pymysql.cursors
from fixture.orm import ORMFixture
from models.group import Group
from fixture.application import Application
from fixture.contact import ContactHelper
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
app = Application

try:
    #ContactHelper.add_contact_to_group(random.choice(db.get_contacts_not_in_group(Group(id="185")), Group(id="185")))
    l = db.get_contacts_in_group(Group(id="135"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()