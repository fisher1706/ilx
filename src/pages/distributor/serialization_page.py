from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class SerializationPage(DistributorPortalPage):
    serial_number_body = {
        "number": None,
        "lot": None,
        "dateManufacture": None,
        "dateShipment": None,
        "dateExpiration": None,
        "dateWarrantyExpires": None
    }
    xpath_save_serial_number = f"{L.button_type}/span[text()='Save']"

    def add_serial_number(self, serial_number_body):
        self.element(L.drop_down_button).click()
        self.element(L.role_menu+L.role_menuitem).click()
        for field in serial_number_body.keys():
            self.input_by_name(field, serial_number_body[field])
        self.element(self.xpath_save_serial_number).click()
        self.dialog_should_not_be_visible()

    def check_last_serial_number(self, serial_number_body):
        table_cells = {
            "Serial Number": serial_number_body["number"],
            "Lot": serial_number_body["lot"],
            "Status": serial_number_body.get("status"),
            "DoS (Date of Shipment)": serial_number_body["dateShipment"],
            "DoM (Date of Manufacture)": serial_number_body["dateManufacture"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_outdated(cell, value)

    def update_last_serial_number(self, serial_number_body):
        self.element(L.last_role_row + L.edit_button).click()
        for field in serial_number_body.keys():
            self.input_by_name(field, serial_number_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def update_last_serial_number_status(self, status):
        self.element(L.last_role_row + L.edit_status_button).click()
        self.element(f"{L.dialog}{L.role_button}//div[text()='{status}']").click()
        self.dialog_should_not_be_visible()

    def delete_last_serial_number(self, number):
        self.element(L.last_role_row + L.remove_button).click()
        self.element(L.dialog + f"//pre[text()='{number}']")
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def import_serial_numbers(self, serial_numbers):
        Tools.generate_csv("serial_numbers.csv", serial_numbers)
        self.import_csv(L.file_upload, "serial_numbers.csv")
        self.element(L.successfully_imported_msg).get()
