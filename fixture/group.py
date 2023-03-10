from model import group
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page_from_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page_in_header(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page_in_header()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_in_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page_from_confirmation()
        self.group_cache = None

    def fill_in_group_form(self, group):
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page_in_header()
        self.select_group_by_index(index)
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page_from_confirmation()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page_in_header()
        self.select_group_by_index(index)
        # initiate group modification
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        # fill in group form
        self.fill_in_group_form(new_group_data)
        # submit the form for changed group (click Update)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page_from_confirmation()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page_in_header()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page_in_header()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, group_id=id))
        return list(self.group_cache)
