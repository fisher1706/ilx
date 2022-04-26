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
    table_cells_checkbox = {
        "Process.Fee": True,
        "SupplyForce": True,
        "User Data": True,
        "Agreements": True,
        "Taxes": True,
        "Level": None,
        "Billing Info": True,
        "Bill by all Ship-tos": True
    }

    def create_distributor(self, distributor_body, checkbox_list):
        check_mark = self.element(L.check_mark).count()
        self.element(L.add_button).click()
        self.element("//*[@id='distributor-create-form']/div/div[1]/div[10]/div/fieldset/label/span[1]/span[1]/input").click()
        for checkbox in checkbox_list:
            self.select_checkbox_in_dialog_by_name(checkbox)
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(1), distributor_body.pop("country"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(2), distributor_body.pop("state"))
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(3), distributor_body.pop("ship_to_level"))
        for field in distributor_body.keys():
            self.input_by_name(field, distributor_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        return check_mark

    def check_last_distributor(self, distributor_body, state_short_code, table_cells_checkbox, check_mark):
        primary_address = " ".join([distributor_body["address.line1"], distributor_body["address.line2"], distributor_body["address.city"], state_short_code, distributor_body["address.zipCode"]])
        table_cells = {
            "Name": distributor_body["name"],
            "External Distributor Number": distributor_body["externalDistributorNumber"],
            "Invoice Email": distributor_body["invoiceEmail"],
            "Primary Address": primary_address,
            "Billing Delay": distributor_body["billingDelay"],
            "Country": distributor_body["country"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_by_header(cell, value)
        for cell in table_cells_checkbox.keys():
            if table_cells_checkbox[cell]:
                self.element(L.check_mark).get()
        checked = sum(1 for value in table_cells_checkbox.values() if value)
        assert self.element(L.check_mark).count() == check_mark+checked, "Incorrect number of checkboxes"

    def update_last_distributor(self, distributor_body, checkbox_list):
        self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
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
        self.element(L.get_indexed(L.remove_button, self.get_table_rows_number())).click()
        self.delete_dialog_should_be_about(full_name)
        self.element(L.confirm_button).click()
        self.dialog_should_not_be_visible()
