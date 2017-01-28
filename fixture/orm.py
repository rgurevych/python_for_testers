from pony.orm import *
from datetime import datetime
from models.group import Group
from models.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind("mysql", host=host, database=name, user=user, password=password, autocommit=True, conv=conv)
        self.db.generate_mapping()

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        first_name = Optional(str, column="firstname")
        last_name = Optional(str, column="lastname")
        deprecated = Optional(datetime, column="deprecated")

    def convert_groups(self, orm_groups):
        def convert(orm_group):
            return Group(id=str(orm_group.id), name=orm_group.name, header=orm_group.header, footer=orm_group.footer)
        return list(map(convert, orm_groups))

    def convert_contacts(self, orm_contacts):
        def convert(orm_contact):
            return Contact(id=str(orm_contact.id), first_name=orm_contact.first_name, last_name=orm_contact.last_name)
        return list(map(convert, orm_contacts))

    @db_session
    def get_group_list(self):
        return self.convert_groups(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts(select(c for c in ORMFixture.ORMContact if c.deprecated is None))