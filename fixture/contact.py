import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from model.contact import Contact
from selenium.webdriver.support import expected_conditions as EC


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def init_contact_creation_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page_in_header(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element(By.CSS_SELECTOR, "a[href='./']").click()

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
        self.contact_cache = None

    def fill_in_contact_form_without_group(self, contact):
        self.change_field_value("firstname", contact.contact_first_name)
        self.change_field_value("lastname", contact.contact_last_name)
        self.change_field_value("address", contact.contact_main_address)

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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_in_header()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # TODO: there is an alert in Firefox only, we need to skip next step in Chrome / Edge
        self.app.alert_is_present()
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page_in_header()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_in_contact_form_without_group(contact)
        # submit contact form modification (click Update)
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.return_to_home_page_from_confirmation()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_in_header()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.open_home_page_in_header()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        contact_first_name = wd.find_element_by_name("firstname").get_attribute("value")
        contact_last_name = wd.find_element_by_name("lastname").get_attribute("value")
        contact_main_address = wd.find_element_by_xpath("//textarea[@name='address']").get_attribute("value")
        contact_homephone = wd.find_element_by_name("home").get_attribute("value")
        contact_mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        contact_workphone = wd.find_element_by_name("work").get_attribute("value")
        contact_secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        contact_first_email = wd.find_element_by_xpath("//input[@name='email']").get_attribute("value")
        contact_second_email = wd.find_element_by_xpath("//input[@name='email2']").get_attribute("value")
        contact_third_email = wd.find_element_by_xpath("//input[@name='email3']").get_attribute("value")
        return Contact(
            contact_id=contact_id,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            contact_main_address=contact_main_address,
            contact_homephone=contact_homephone,
            contact_mobilephone=contact_mobilephone,
            contact_workphone=contact_workphone,
            contact_secondaryphone=contact_secondaryphone,
            contact_first_email=contact_first_email,
            contact_second_email=contact_second_email,
            contact_third_email=contact_third_email
        )

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        text = wd.find_element_by_id("content").text
        contact_homephone = re.search("H: (.*)", text).group(1)
        contact_mobilephone = re.search("M: (.*)", text).group(1)
        contact_workphone = re.search("W: (.*)", text).group(1)
        contact_secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(
            contact_homephone=contact_homephone,
            contact_mobilephone=contact_mobilephone,
            contact_workphone=contact_workphone,
            contact_secondaryphone=contact_secondaryphone
        )

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_home_page_in_header()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page_in_header()
            self.contact_cache = []
            # find all elements with tr tag and build a list of these elements (table lines from the table)
            contacts_table_rows = wd.find_elements_by_xpath(".//*[@id='maintable']/tbody/tr")
            # remove header line (first row)
            contacts_table_rows.remove(contacts_table_rows[0])

            for row in contacts_table_rows:
                # for each line (or a table row, or element in the contact_table_row list) I search for a single cell
                # build a list of cells that belong to 1 row, recognising them by tag
                cells = row.find_elements_by_tag_name("td")
                # in a row, check for unique input tag for a checkbox and get its id
                id = row.find_element(By.TAG_NAME, "input").get_attribute("value")
                # grabbing necessary text attributes from needed cells
                first_name = cells[2].text
                last_name = cells[1].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                main_address = cells[3].text
                self.contact_cache.append(
                    Contact(
                        contact_id=id,
                        contact_first_name=first_name,
                        contact_last_name=last_name,
                        contact_main_address=main_address,
                        all_emails_from_home_page=all_emails,
                        all_phones_from_home_page=all_phones))
        return list(self.contact_cache)
