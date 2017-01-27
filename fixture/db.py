import pymysql.cursors
from models.group import Group
from models.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        #self.connection.autocommit = True


    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer)=row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
            #self.connection.commit()
        return group_list


    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook WHERE deprecated IS NULL")
            for row in cursor.fetchall():
                (id, first_name, last_name)=row
                contact_list.append(Contact(id=str(id), first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
            #self.connection.commit()
        return contact_list


    def destroy(self):
        self.connection.close()