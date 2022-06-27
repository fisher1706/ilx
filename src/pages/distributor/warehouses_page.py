from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class WarehousesPage(DistributorPortalPage):
    warehouse_body = {
        "name": None,
        "number": None,
        "address.line1": None,
        "address.line2": None,
        "address.city": None,
        "address.zipCode": None,
        "state": None,
        "contactEmail": None,
        "invoiceEmail": None,
        "timezone": None
    }

    def create_warehouse(self, warehouse_body):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), warehouse_body.pop("state"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), warehouse_body.pop("timezone"))
        for field in warehouse_body.keys():
            self.input_by_name(field, warehouse_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)

    def check_last_warehouse(self, warehouse_body):
        table_cells = {
            "Warehouse name": warehouse_body["name"],
            "Warehouse number": warehouse_body["number"],
            "Timezone": warehouse_body["timezone"],
            "Contact email": warehouse_body["contactEmail"],
            "Invoice email": warehouse_body["invoiceEmail"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def update_last_warehouse(self, warehouse_body):
        self.element(L.last_role_row+L.edit_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), warehouse_body.pop("state"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), warehouse_body.pop("timezone"))
        for field in warehouse_body.keys():
            self.input_by_name(field, warehouse_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def delete_last_warehouse(self, value):
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(value)
        self.element(L.confirm_button).click()
        self.dialog_should_not_be_visible()
