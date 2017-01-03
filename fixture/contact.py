
from models.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add(self, contact):
        wd = self.app.wd
        # initiate adding contact
        wd.find_element_by_link_text("add new").click()
        # fill in some fields
        self.fill_contact_from(contact)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def fill_contact_from(self, contact):
        wd = self.app.wd
        self.type_in_contact_field("firstname", contact.first_name)
        self.type_in_contact_field("lastname", contact.last_name)
        self.type_in_contact_field("mobile", contact.mobile_phone)
        self.type_in_contact_field("email", contact.email)


    def type_in_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def edit_first_contact(self, contact):
        wd = self.app.wd
        # initiate editing first contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update fields
        self.fill_contact_from(contact)
        # complete editing
        wd.find_element_by_name("update").click()


    def delete_first_contact(self):
        wd = self.app.wd
        #select first contact
        wd.find_element_by_name("selected[]").click()
        #delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #confirm deletion
        wd.switch_to_alert().accept()


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    def get_contacts_list(self):
        wd = self.app.wd
        contacts_list = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts_list.append(Contact(first_name=text, id=id))
        return contacts_list