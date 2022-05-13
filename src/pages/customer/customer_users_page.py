from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L

class CustomerUsersPage(CustomerPortalPage):
    customer_user_body = {
        "firstName": None,
        "lastName": None,
        "email": None,
        "role": None,
        "shiptos": None
    }

    def create_customer_user(self, customer_user_body):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_user_body.pop("role"))
        self.manage_shipto(customer_user_body.pop("shiptos"), L.dialog)
        for field in customer_user_body.keys():
            self.input_by_name(field, customer_user_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def check_last_customer_user(self, customer_user_body):
        self.open_last_page()
        table_cells = {
            "Email": customer_user_body["email"],
            "First Name": customer_user_body["firstName"],
            "Last Name": customer_user_body["lastName"],
            "Security Group": customer_user_body["role"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_outdated(cell, value)

    def update_last_customer_user(self, customer_user_body):
        self.element(L.last_role_row).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_user_body.pop("role"))
        self.manage_shipto(customer_user_body.pop("shiptos"), L.dialog)
        for field in customer_user_body.keys():
            self.input_by_name(field, customer_user_body[field])
        self.element(L.submit_button).click()

    def delete_last_customer_user(self):
        full_name = self.get_last_table_item_text_by_header_outdated("First Name")
        full_name += " " + self.get_last_table_item_text_by_header_outdated("Last Name")
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
