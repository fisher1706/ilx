from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L

class RfidPage(DistributorPortalPage):
    xpath_rfid_add = f"{L.dialog+L.button_type}//span[text()='Add']"

    def add_rfid_label(self, label=None):
        if label is None:
            label = Tools.random_string_u()
        self.element(L.add_button).click()
        self.input_by_name("labelId", label)
        self.element(self.xpath_rfid_add).click()
        self.dialog_should_not_be_visible()
        return label

    def check_last_rfid_label(self, label, status):
        self.check_last_table_item_outdated("RFID", label)
        self.check_last_table_item_outdated("State", status)

    def update_last_rfid_label_status(self, status):
        self.element(L.last_role_row + L.edit_status_button).click()
        self.element(f"{L.dialog}{L.role_button}//span[text()='{status}']").click()
        self.dialog_should_not_be_visible()

    def unassign_last_rfid_label(self):
        self.element(L.last_role_row + L.unassign_button).click()
        self.element(L.get_button_by_name("Yes, unassign EPC")).click()
        self.dialog_should_not_be_visible()

    def import_rfid_as_available(self, rfids):
        Tools.generate_csv("rfids_as_available.csv", rfids)
        self.import_csv(L.upload_rfid_available, "rfids_as_available.csv")
        self.element(L.successfully_imported_msg).get()

    def import_rfid(self, rfids):
        Tools.generate_csv("rfids.csv", rfids)
        self.import_csv(L.upload_rfid_csv, "rfids.csv")
        self.element(L.successfully_imported_msg).get()
