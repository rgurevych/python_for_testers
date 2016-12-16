# для запуска в браузере Chrome откомментить следующую строку:
from selenium.webdriver.chrome.webdriver import WebDriver
# для запуска в браузере Firefox откомментить следующие две строки:
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()     #откомментировать для запуска в Chrome
        # self.wd = WebDriver(firefox_binary=FirefoxBinary("C:/Program Files/Firefox_ESR/firefox.exe"))
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_app_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()