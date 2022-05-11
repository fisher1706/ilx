from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class VmiPage(DistributorPortalPage):
    location_body = {
        "sku": None,
        "orderingConfig.currentInventoryControls.min": None,
        "orderingConfig.currentInventoryControls.max": None,
        "attributeName1": None,
        "attributeValue1": None,
        "customerSku": None,
        "type": None
    }
    xpath_button_bulk_operations = f"{L.xpath_button_type}//span[text()='Bulk operations']"

    def follow_location_url(self, customer_id=None, shipto_id=None):
        if customer_id is None:
            customer_id = self.data.customer_id
        if shipto_id is None:
            shipto_id = self.data.shipto_id
        self.follow_url(f"{self.url.distributor_portal}/customers/{customer_id}/shiptos/{shipto_id}#vmi-list")

    def create_location(self, location_body):
        self.click_id(L.id_add_button)
        self.select_in_dropdown_via_input(L.get_dropdown_in_dialog(1), location_body.pop("sku"), span=True)
        for field in location_body.keys():
            self.input_by_name(field, location_body[field])
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()
        

    def check_last_location(self, location_body):
        self.open_last_page()
        table_cells = {
            "Distributor SKU": location_body["sku"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_outdated(cell, value)

    def import_location(self, locations):
        Tools.generate_csv("locations.csv", locations)
        self.click_id(L.id_item_action_import)
        self.import_csv(L.id_file_upload, "locations.csv")
        self.get_element_by_xpath(L.xpath_successfully_imported_msg)
        
