
from models.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def add(self, contact):
        wd = self.app.wd
        self.open_homepage()
        # initiate adding contact
        wd.find_element_by_link_text("add new").click()
        # fill in some fields
        self.fill_contact_form(contact)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.open_homepage()
        self.contact_cache = None


    def fill_contact_form(self, contact):
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
        self.edit_any_contact(contact, 0)


    def edit_any_contact(self, contact, index):
        wd = self.app.wd
        self.open_homepage()
        # initiate editing first contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # update fields
        self.fill_contact_form(contact)
        # complete editing
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contact_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_any_contact(0)


    def delete_any_contact(self, index):
        wd = self.app.wd
        self.open_homepage()
        #select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.open_homepage()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    #def return_to_home_page(self):
    #    wd = self.app.wd
    #    wd.find_element_by_link_text("home page").click()


    def open_homepage(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()


    contact_cache = None


    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=cells[2].text, last_name=cells[1].text, id=id))
        return list(self.contact_cache)