# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import unittest


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
        wd = self.wd
        # open home page
        wd.get("https://localhost/addressbook/group.php")
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # init new contact creation from home page
        wd.find_element_by_link_text("add new").click()
        # add a contact without group from home page
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("First name")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Last name")
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to home page from confirmation screen
        wd.find_element_by_link_text("home page").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
