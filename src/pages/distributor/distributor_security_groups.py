from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class DistributorSecurityGroups(DistributorPortalPage):
    distributor_security_group_body = {
        "name": None,
        "checked": None,
    }

    def open_security_groups(self):
        self.sidebar_users()
        self.click_tab_by_name("Security Groups")

    def create_security_group(self, distributor_security_group_body):
        self.element(L.add_button).click()
        self.input_by_name("name", distributor_security_group_body["name"])
        for checkbox in range(1, 4):
            self.select_checkbox(L.get_indexed(L.checkbox, checkbox))
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)
        self.check_last_table_item("Group name", distributor_security_group_body["name"])

    def check_security_group(self, distributor_security_group_body):
        self.element(L.last_role_row + L.view_button).click()
        text = self.element("//input[@name='name']").get().get_attribute("value")
        assert text == distributor_security_group_body["name"], f"Name contains incorrect text: {text}"
        for checkbox in range(1, 4):
            if distributor_security_group_body["checked"]:
                self.checkbox_should_be(L.get_indexed(L.checkbox, checkbox), True)
            else:
                self.checkbox_should_be(L.get_indexed(L.checkbox, checkbox), False)
        self.element("//a[@href='/distributor/users-groups#security-groups']").click()
        self.last_page(10)
        self.check_last_table_item("Group name", distributor_security_group_body["name"])

    def update_security_group(self, distributor_security_group_body):
        self.element(L.last_role_row + L.edit_button).click()
        self.input_by_name("name", distributor_security_group_body["name"])
        self.element(L.submit_button).click()
        for checkbox in range(1, 4):
            if distributor_security_group_body["checked"]:
                self.select_checkbox(L.get_indexed(L.checkbox, checkbox))
            else:
                self.unselect_checkbox(L.get_indexed(L.checkbox, checkbox))
        self.element(f"({L.save_button})[last()]").click()
        self.check_reset_permissions()
        self.element("//a[@href='/distributor/users-groups#security-groups']").click()
        self.element(L.reload_button).click()
        self.last_page(10)
        self.check_last_table_item("Group name", distributor_security_group_body["name"])

    def delete_security_group(self, distributor_security_group_body):
        self.element(L.last_role_row + L.remove_button).click()
        self.delete_dialog_should_be_about(distributor_security_group_body["name"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def check_reset_permissions(self):
        for checkbox in range(5, 36):
            self.select_checkbox(L.get_indexed(L.checkbox, checkbox))
        self.element(L.get_indexed(L.button_reset, 2)).click()
        for checkbox in range(5, 36):
            self.checkbox_should_be(L.get_indexed(L.checkbox, checkbox), False)
