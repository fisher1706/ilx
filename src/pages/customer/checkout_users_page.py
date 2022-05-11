from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L

class CheckoutUsersPage(CustomerPortalPage):
    checkout_user_body = {
        "firstName": None,
        "lastName": None,
        "fob": None,
        "passCode": None,
        "email": None,
        "phone": None
    }

    def create_checkout_user(self, checkout_user_body, first_group=False):
        start_number_of_rows = self.get_table_rows_number()
        self.element(L.add_button).click()
        for field in checkout_user_body.keys():
            self.input_by_name(field, checkout_user_body[field])
        if first_group:
            self.select_checkbox(L.checkbox)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.element(L.table_row).wait_elements_number(start_number_of_rows+1)

    def check_last_checkout_user(self, checkout_user_body):
        table_cells = {
            "Email": checkout_user_body["email"],
            "First Name": checkout_user_body["firstName"],
            "Last Name": checkout_user_body["lastName"],
            "FOB": checkout_user_body["fob"],
            "Passcode": checkout_user_body["passCode"],
            "Role": "Checkout User",
            "Phone": checkout_user_body["phone"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_by_header(cell, value)

    def update_last_checkout_user(self, checkout_user_body, first_group=False):
        self.element(L.last_role_row).click()
        for field in checkout_user_body.keys():
            self.input_by_name(field, checkout_user_body[field])
        if first_group:
            self.select_checkbox(L.checkbox)
        self.element(L.submit_button).click()

    def delete_last_checkout_user(self):
        full_name = self.get_last_table_item_text_by_header("First Name")
        full_name += " " + self.get_last_table_item_text_by_header("Last Name")
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def import_checkout_user(self, checkout_users):
        Tools.generate_csv("checkout_users.csv", checkout_users)
        self.import_csv(L.file_upload, "checkout_users.csv")
        self.element(L.successfully_imported_msg).get()
