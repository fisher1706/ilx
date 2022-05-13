from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class ShiptoPage(DistributorPortalPage):
    shipto_body = {
        "name": None,
        "number": None,
        "poNumber": None,
        "address.zipCode": None,
        "address.line1": None,
        "address.line2": None,
        "address.city": None,
        "state": None,
        "notes": None,
        "contactId": None
    }

    def follow_shipto_url(self):
        self.follow_url(f"{self.url.distributor_portal}/customers/{self.data.customer_id}#shiptos")

    def create_shipto(self, shipto_body):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), shipto_body.pop("state"))
        for field in shipto_body.keys():
            self.input_by_name(field, shipto_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)

    def check_last_shipto(self, shipto_body):
        table_cells = {
            "Shipto Number": shipto_body["number"],
            "Shipto Name": shipto_body["name"],
            "PO Numbers": shipto_body["poNumber"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def update_last_shipto(self, shipto_body, actions_pop_up=True):
        if actions_pop_up:
            self.element(L.last_role_row + L.actions_button).click()
        self.element(L.last_role_row + L.shipto_info_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), shipto_body.pop("state"))
        for field in shipto_body.keys():
            self.input_by_name(field, shipto_body[field])
        self.element(L.submit_button).click()
        self.wait_until_progress_bar_loaded()

    def delete_last_shipto(self, actions_pop_up=True):
        name = self.get_last_table_item_text_by_header("Shipto Number")
        if actions_pop_up:
            self.element(L.last_role_row + L.actions_button).click()
        self.element(L.last_role_row + L.remove_button).click()
        self.delete_dialog_should_be_about(name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
