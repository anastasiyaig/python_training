# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import unittest

from contact import Contact


def is_alert_present(self):
    try:
        self.wd.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact_without_group(self):
        self.login(username="admin", password="secret")
        self.add_contact_without_group(Contact(contact_first_name="First name", contact_last_name="Last name"))
        self.logout()

    def return_to_home_page_from_confirmation(self, wd):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def add_contact_without_group(self, contact):
        wd = self.wd
        self.init_contact_creation_home_page(wd)
        # add a contact without group (none value) from home page
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.contact_first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.contact_last_name)
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page_from_confirmation(wd)

    def init_contact_creation_home_page(self, wd):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
