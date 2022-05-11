from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L
from glbl import Error

class CheckoutGroupsPage(CustomerPortalPage):
    checkout_group_body = {
        "name": None,
        "email": None
    }
    id_associate = "item-action-associate"

    def create_checkout_group(self, checkout_group_body):
        
        start_number_of_rows = self.get_table_rows_number()
        self.element(L.add_button).click()
        for field in checkout_group_body.keys():
            self.input_by_name(field, checkout_group_body[field])
        self.element(L.get_dropdown_in_dialog(1)).click()
        self.element(L.dropdown_list_item+"/div").click()
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.element(L.table_row).wait_elements_number(start_number_of_rows+1)

    def check_new_checkout_group(self, checkout_group_body, row, owner=None, shipto=None):
        table_cells = {
            "Checkout Group Name": checkout_group_body["name"],
            "Checkout Group Email": checkout_group_body["email"],
            "Owner": owner,
            "Associated Shipto": shipto
        }
        for cell, value in table_cells.items():
            self.check_table_item_by_header(row, cell, value)

    def update_new_checkout_group(self, checkout_group_body, row):
        self.element(L.get_indexed(L.table_row, row)).click()
        self.element(L.get_dropdown_in_dialog(1)).click()
        self.element(L.dropdown_list_item+"/div[last()]").click()
        for field in checkout_group_body.keys():
            self.input_by_name(field, checkout_group_body[field])
        self.element(L.submit_button).click()

    def delete_new_checkout_group(self, row):
        full_name = self.get_table_item_text_by_header("Checkout Group Name", row)
        self.element(L.get_indexed(L.table_row, row)+L.remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def assign_shipto(self, shipto_number):
        self.element(self.id_associate).click()
        self.element(L.select_button).get()
        for index in range(1, self.element(L.dialog+L.table_row).click()+1):
            if self.element(L.get_table_item_in_dialog(index, 1)).get() == str(shipto_number):
                self.element(L.get_indexed(L.dialog+L.table_row+L.button_type, index)).click()
                break
        else:
            Error.error(f"There is no shipto '{shipto_number}'")
        self.element(L.button_save).click()
        self.dialog_should_not_be_visible()

    def check_assigned_shipto(self, shipto_body, row):
        table_cells = {
            "Shipto Number": shipto_body["number"],
            "Shipto Name": shipto_body["name"],
            "Address": [shipto_body["address"]["zipCode"], shipto_body["address"]["line1"], shipto_body["address"]["line2"], shipto_body["address"]["city"]],
            "Supplier": self.data.distributor_name
        }
        for cell, value in table_cells.items():
            self.check_table_item_by_header(row, cell, value)

    def unassign_shipto(self, row):
        shipto_number = self.get_table_item_text_by_header("Shipto Number", row)
        self.element(L.get_indexed(L.table_row, row)+L.remove_button).click()
        self.delete_dialog_should_be_about(shipto_number)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def assign_user(self, user_email):
        self.element(self.id_associate).click()
        self.element(L.select_button).get()
        for index in range(1, self.element(L.dialog+L.table_row).count()+1):
            if self.element(L.get_table_item_in_dialog(index, 4)).text() == str(user_email):
                self.element(L.get_indexed(L.dialog+L.table_row+L.button_type, index)).click()
                break
        else:
            Error.error(f"There is no shipto '{user_email}'")
        self.element(L.button_save).click()
        self.dialog_should_not_be_visible()
        

    def check_assigned_user(self, user_body, row):
        table_cells = {
            "First Name": user_body["firstName"],
            "Last Name": user_body["lastName"],
            "Email": user_body["email"]
        }
        for cell, value in table_cells.items():
            self.check_table_item_by_header(row, cell, value)

    def unassign_user(self, row):
        full_name = self.get_last_table_item_text_by_header("First Name")
        full_name += " " + self.get_last_table_item_text_by_header("Last Name")
        self.element(L.get_indexed(L.table_row, row)+L.remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
