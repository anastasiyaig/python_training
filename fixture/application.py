from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/index.php")

    def alert_is_present(self, timeout=3):
        wd = self.wd
        WebDriverWait(wd, timeout).until(EC.alert_is_present())
        wd.switch_to.alert.accept()

    def destroy(self):
        self.wd.quit()
