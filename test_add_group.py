# -*- coding: utf-8 -*-
# для запуска в браузере Chrome откомментить следующую строку:
# from selenium.webdriver.chrome.webdriver import WebDriver

# для запуска в браузере Firefox откомментить следующие две строки:
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        #self.wd = WebDriver()
        self.wd = WebDriver(firefox_binary=FirefoxBinary("C:/Program Files/Firefox_ESR/firefox.exe"))
        self.wd.implicitly_wait(60)

    def open_app_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        self.open_app_page(wd)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_new_group(self, wd, group):
        self.open_groups_page(wd)
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
        self.return_to_groups_page(wd)

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_normal_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_group(wd, Group(name="test group 1", header="header 1", footer="footer 1"))
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
