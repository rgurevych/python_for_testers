import re
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
        self.type_in_contact_field("address", contact.address)
        self.type_in_contact_field("home", contact.home_phone)
        self.type_in_contact_field("work", contact.work_phone)
        self.type_in_contact_field("mobile", contact.mobile_phone)
        self.type_in_contact_field("fax", contact.fax)
        self.type_in_contact_field("email", contact.email_1)
        self.type_in_contact_field("email2", contact.email_2)
        self.type_in_contact_field("email3", contact.email_3)


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
        # initiate editing contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # update fields
        self.fill_contact_form(contact)
        # complete editing
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contact_cache = None


    def edit_contact_by_id(self, contact):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']/img" % contact.id).click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_homepage()
        self.contact_cache = None


    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_any_contact(0)


    def delete_any_contact(self, index):
        wd = self.app.wd
        self.open_homepage()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.open_homepage()
        self.contact_cache = None


    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_id(id).click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #confirm deletion
        wd.switch_to_alert().accept()
        self.open_homepage()
        self.contact_cache = None


    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    def open_homepage(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()


    contact_cache = None


    def get_contact_list(self):
        self.open_homepage()
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                emails = cells[4].text
                phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                                                  all_phones_homepage=phones, all_emails_homepage=emails))
        return list(self.contact_cache)


    def get_contact_data_editpage(self, index):
        wd = self.app.wd
        self.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, email_1=email_1, email_2=email_2, email_3=email_3,
                       address=address, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       fax=fax, id=id)


    def get_contact_data_viewpage(self, index):
        wd = self.app.wd
        self.open_homepage()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, fax=fax)


    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_id(contact.id).click()
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group.id).click()
        wd.find_element_by_xpath("//input[@name='add']").click()
        self.open_homepage()
        self.contact_cache = None


    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.open_homepage()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='%s']" % group.id).click()
        wd.find_element_by_id(contact.id).click()
        wd.find_element_by_xpath("//input[@name='remove']").click()
        self.open_homepage()
        self.contact_cache = None
