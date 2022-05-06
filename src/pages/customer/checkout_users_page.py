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
        self.click_id(L.id_add_button)
        for field in checkout_user_body.keys():
            self.input_by_name(field, checkout_user_body[field])
        if first_group:
            self.select_checkbox(L.xpath_checkbox)
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()
        
        self.elements_count_should_be(L.xpath_table_row, start_number_of_rows+1)

    def check_new_checkout_user(self, checkout_user_body, row):
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
            self.check_table_item_by_header(row, cell, value)

    def update_new_checkout_user(self, checkout_user_body, row, first_group=False):
        
        self.click_xpath(L.xpath_by_count(L.xpath_table_row, row))
        for field in checkout_user_body.keys():
            self.input_by_name(field, checkout_user_body[field])
        if first_group:
            self.select_checkbox(L.xpath_checkbox)
        self.click_xpath(L.xpath_submit_button)

    def delete_new_checkout_user(self, row):
        full_name = self.get_table_item_text_by_header("First Name", row)
        full_name += " " + self.get_table_item_text_by_header("Last Name", row)
        
        self.get_element_by_xpath(L.xpath_by_count(L.xpath_table_row, row)+L.xpath_remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()

    def import_checkout_user(self, checkout_users):
        Tools.generate_csv("checkout_users.csv", checkout_users)
        self.import_csv(L.id_file_upload, "checkout_users.csv")
        self.get_element_by_xpath(L.xpath_successfully_imported_msg)
        
