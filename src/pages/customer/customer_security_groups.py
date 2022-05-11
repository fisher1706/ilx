from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L

class CustomerSecurityGroups(CustomerPortalPage):
    security_group_body = {
        "name": None,
        "checked": None,
    }

    def open_security_groups(self):
        self.sidebar_users_and_groups()
        self.click_tab_by_name("Security Groups")

    def create_security_group(self, security_group_body):
        self.element(L.add_button).click()
        self.input_by_name("name", security_group_body["name"])
        for checkbox in range(1, 4):
            self.select_checkbox(L.get_indexed(L.checkbox, checkbox))
        self.element(L.submit_button).click()
        self.wait_until_progress_bar_loaded()
        self.element(L.table_row).get()

    def check_security_group(self, security_group_body):
        self.element_should_have_text(L.get_last_table_item_outdated(1), security_group_body["name"])
        self.element(L.last_role_row+L.view_button).click()
        text = self.element("//input[@name='name']").get().get_attribute("value")
        assert text == security_group_body["name"], f"Incorrect name of the security group. Now: {text}. Expected: {security_group_body['name']}"
        for checkbox in range(1, 4):
            if security_group_body["checked"]:
                self.checkbox_should_be(L.get_indexed(L.checkbox, checkbox), True)
            else:
                self.checkbox_should_be(L.get_indexed(L.checkbox, checkbox), False)
        self.element("//a[@href='/customer/users-and-groups#security-groups']").click()

    def update_security_group(self, security_group_body):
        self.element(L.last_role_row+L.edit_button).click()
        self.wait_until_progress_bar_loaded()
        self.element("//input[@name]").clear()
        self.input_by_name("name", security_group_body["name"])
        self.element(L.submit_button).click()
        self.wait_until_progress_bar_loaded()
        for checkbox in range(1, 4):
            self.unselect_checkbox(L.get_indexed(L.checkbox, checkbox))
        self.element(f"({L.submit_button})[last()]").click()
        self.wait_until_progress_bar_loaded()
        self.element("//a[@href='/customer/users-and-groups#security-groups']").click()

    def delete_security_group(self, security_group_body):
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(security_group_body["name"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
