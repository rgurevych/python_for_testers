# для запуска в браузере Chrome откомментить следующую строку:
from selenium.webdriver.chrome.webdriver import WebDriver

# для запуска в браузере Firefox откомментить следующие две строки:
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()     #откомментировать для запуска в Chrome
        # self.wd = WebDriver(firefox_binary=FirefoxBinary("C:/Program Files/Firefox_ESR/firefox.exe"))
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def open_app_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def create_new_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # start new group creation
        wd.find_element_by_name("new").click()
        # complete new group creation form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation form
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def add_new_contact(self, contact):
        wd = self.wd
        # initiate adding contact
        wd.find_element_by_link_text("add new").click()
        # fill in some fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # create contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def destroy(self):
        self.wd.quit()