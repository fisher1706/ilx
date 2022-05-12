from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class DistributorUsersPage(DistributorPortalPage):
    distributor_user_body = {
        "firstName": None,
        "lastName": None,
        "email": None,
        "role": None,
        "warehouses": None,
        "position": None
    }

    distributor_superuser_body = {
        "firstName": None,
        "lastName": None,
        "email": None,
        "position": None
    }

    def create_distributor_user(self, distributor_user_body):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), distributor_user_body.pop("role"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), distributor_user_body.pop("position"))
        for checkbox in distributor_user_body.pop("warehouses"):
            self.select_checkbox_in_dialog_by_name(checkbox)
        for field in distributor_user_body.keys():
            self.input_by_name(field, distributor_user_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)
        self.check_last_table_item("Email", distributor_user_body["email"])

    def check_last_distributor_user(self, distributor_user_body):
        table_cells = {
            "Email": distributor_user_body["email"],
            "First name": distributor_user_body["firstName"],
            "Last name": distributor_user_body["lastName"],
            "Role": distributor_user_body["role"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def update_last_distributor_user(self, distributor_user_body):
        self.element(L.last_role_row+L.edit_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), distributor_user_body.pop("role"))
        for checkbox in distributor_user_body.pop("warehouses"):
            self.select_checkbox_in_dialog_by_name(checkbox)
        for field in distributor_user_body.keys():
            self.input_by_name(field, distributor_user_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def delete_last_distributor_user(self, value):
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(value)
        self.element(L.confirm_button).click()
        self.dialog_should_not_be_visible()

    def create_distributor_super_user(self, distributor_superuser_body):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), distributor_superuser_body.pop("role"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), distributor_superuser_body.pop("position"))
        for field in distributor_superuser_body.keys():
            self.input_by_name(field, distributor_superuser_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)
        self.check_last_table_item("Email", distributor_superuser_body["email"])

    def check_last_distributor_super_user(self, distributor_superuser_body):
        table_cells = {
            "Email": distributor_superuser_body["email"],
            "First name": distributor_superuser_body["firstName"],
            "Last name": distributor_superuser_body["lastName"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def update_last_distributor_super_user(self, distributor_superuser_body):
        self.element(L.last_role_row+L.edit_button).click()
        for field in distributor_superuser_body.keys():
            self.input_by_name(field, distributor_superuser_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
