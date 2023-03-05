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
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
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
        WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))

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

    def get_contacts_list(self):
        wd = self.app.wd
        self.open_home_page_in_header()
        contacts_list = []
        # find all elements with tr tag and build a list of these elements (table lines from the table)
        contacts_table_rows = wd.find_elements_by_xpath(".//*[@id='maintable']/tbody/tr")
        # remove header line (first row)
        contacts_table_rows.remove(contacts_table_rows[0])

        for row in contacts_table_rows:
            # for each line (or a table row, or element in the contact_table_row list) I search for a single cell
            # build a list of cells that belong to 1 row, recognising them by tag
            cells = row.find_elements(By.TAG_NAME, "td")
            # in a row, check for unique input tag for a checkbox and get its id
            id = row.find_element(By.TAG_NAME, "input").get_attribute("value")
            # grabbing necessary text attributes from needed cells
            first_name = cells[2].text
            last_name = cells[1].text
            contacts_list.append(Contact(contact_first_name=first_name, contact_last_name=last_name, contact_id=id))
        return contacts_list




