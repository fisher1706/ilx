from src.pages.admin.admin_portal_page import AdminPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L

class UniversalCatalogPage(AdminPortalPage):
    universal_product_body = {
        "manufacturerPartNumber": None,
        "manufacturer": None,
        "gtin": None,
        "upc": None
    }

    def create_universal_product(self, product_body):
        self.element(L.add_button).click()
        for field in product_body.keys():
            self.input_by_name(field, product_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def check_last_universal_product(self, product_body):
        table_cells = {
            "UPC": product_body["upc"],
            "GTIN": product_body["gtin"],
            "Manufacturer": product_body["manufacturer"],
            "Manufacturer SKU": product_body["manufacturerPartNumber"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_by_header(cell, value)

    def update_universal_product(self, product_body):
        self.element(L.last_role_row + L.edit_button).click()
        for field in product_body.keys():
            self.input_by_name(field, product_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def delete_universal_product(self):
        self.element(L.last_role_row + L.remove_button).click()
        self.element(L.dialog+L.confirm_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def import_universal_catalog(self, elements):
        Tools.generate_csv("universal_catalog.csv", elements)
        self.import_csv(L.file_upload, "universal_catalog.csv")
        self.element(L.successfully_imported_msg).get()
        self.wait_until_progress_bar_loaded()
