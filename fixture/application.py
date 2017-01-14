from selenium import webdriver
# для запуска в браузере Chrome откомментить следующую строку:
# from selenium.webdriver.chrome.webdriver import WebDriver
# для запуска в браузере Firefox откомментить следующие две строки:
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox(firefox_binary=FirefoxBinary("C:/Program Files/Firefox_ESR/firefox.exe"))
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "opera":
            self.wd == webdriver.Opera()
        else:
            raise ValueError("Unknown browser: %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_app_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()
