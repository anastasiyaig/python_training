from selenium.webdriver.common.by import By

from model import contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def init_contact_creation_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page_in_header(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "a[href='./']").click()
        # wd.find_element_by_link_text("home").click()

    def return_to_home_page_from_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_contact_without_group(self, contact):
        wd = self.app.wd
        self.init_contact_creation_home_page()
        self.fill_in_contact_form_without_group(contact)
        # select None value for the group
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        self.submit_contact_form_creation()
        self.return_to_home_page_from_confirmation()

    def fill_in_contact_form_without_group(self, contact):
        self.change_field_value("firstname", contact.contact_first_name)
        self.change_field_value("lastname", contact.contact_last_name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def submit_contact_form_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Enter']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page_in_header()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # TODO: there is an alert in Firefox only, we need to skip next step in Chrome / Edge
        self.app.alert_is_present()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page_in_header()
        # TODO: might be helpful in future when specifying exact contact to edit
        # wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_in_contact_form_without_group(contact)
        # submit contact form modification (click Update)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page_from_confirmation()

    def count(self):
        wd = self.app.wd
        self.open_home_page_in_header()
        return len(wd.find_elements_by_name("selected[]"))
