from src.pages.admin.admin_portal_page import AdminPortalPage
from src.pages.locator import Locator as L

class DistributorAdminPage(AdminPortalPage):
    distributor_body = {
        "name": None,
        "externalDistributorNumber": None,
        "invoiceEmail": None,
        "address.line1": None,
        "address.line2": None,
        "address.city": None,
        "address.zipCode": None,
        "billingDelay": None,
        "country": None,
        "state": None,
        "ship_to_level": None
    }

    def create_distributor(self, distributor_body, checkbox_list):
        self.element(L.add_button).click()
        for checkbox in checkbox_list:
            self.select_checkbox_in_dialog_by_name(checkbox)
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(1), distributor_body.pop("country"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(2), distributor_body.pop("state"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(3), distributor_body.pop("ship_to_level"))
        for field in distributor_body.keys():
            self.input_by_name(field, distributor_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.open_last_page()
        return self.get_table_rows_number()

    def check_last_distributor(self, distributor_body, state_short_code, number_of_checkboxes, row):
        primary_address = " ".join([distributor_body["address.line1"], distributor_body["address.line2"], distributor_body["address.city"], state_short_code, distributor_body["address.zipCode"]])
        table_cells = {
            "Name": distributor_body["name"],
            "External Distributor Number": distributor_body["externalDistributorNumber"],
            "Invoice Email": distributor_body["invoiceEmail"],
            "Primary Address": primary_address,
            "Billing Delay": distributor_body["billingDelay"],
            "Country": distributor_body["country"]
        }
        for header, value in table_cells.items():
            self.check_table_item_by_header(row, header, value)
        actual_count = self.element(L.get_indexed(L.table_row, row)+L.check_mark).count()
        assert actual_count == number_of_checkboxes, f"Incorrect number of checkboxes. Now: {actual_count}. Should be: {number_of_checkboxes}"

    def update_last_distributor(self, distributor_body, checkbox_list):
        self.element(L.last_role_row + L.edit_button).click()
        for checkbox in checkbox_list:
            self.unselect_checkbox_in_dialog_by_name(checkbox)
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(1), distributor_body.pop("country"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(2), distributor_body.pop("state"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(3), distributor_body.pop("ship_to_level"))
        for field in distributor_body.keys():
            self.input_by_name(field, distributor_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def delete_last_distributor(self):
        full_name = self.get_last_table_item_text_by_header("Name")
        self.element(L.last_role_row + L.remove_button).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.confirm_button).click()
        self.dialog_should_not_be_visible()
