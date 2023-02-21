from model import group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page_from_confirmation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page_in_header(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page_in_header()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill in group form
        self.fill_in_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page_from_confirmation()

    def fill_in_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page_in_header()
        # select (check) first group in the list
        wd.find_element_by_name("selected[]").click()
        # submit group deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page_from_confirmation()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page_in_header()
        # select (check) first group in the list
        wd.find_element_by_name("selected[]").click()
        # initiate group modification
        wd.find_element_by_xpath("//input[@value='Edit group']").click()
        # fill in group form
        self.fill_in_group_form(group)
        # submit the form for changed group (click Update)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page_from_confirmation()

