from models.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # start new group creation
        wd.find_element_by_name("new").click()
        # complete new group creation form
        self.fill_group_form(group)
        # submit group creation form
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None


    def fill_group_form(self, group):
        wd = self.app.wd
        self.type_in_group_field("group_name", group.name)
        self.type_in_group_field("group_header", group.header)
        self.type_in_group_field("group_footer", group.footer)


    def type_in_group_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.edit_any_group(new_group_data, 0)


    def edit_any_group(self, new_group_data, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # initiate editing
        wd.find_element_by_name("edit").click()
        # complete new group creation form
        self.fill_group_form(new_group_data)
        # submit group editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete_first_group(self):
        wd = self.app.wd
        self.delete_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))


    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
