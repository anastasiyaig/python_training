

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def init_contact_creation_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_home_page_from_confirmation(self, wd):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def add_contact_without_group(self, contact):
        wd = self.app.wd
        self.init_contact_creation_home_page()
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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # TODO: there is an alert in Firefox only, we need to skip next step in Chrome / Edge
        self.app.alert_is_present()
