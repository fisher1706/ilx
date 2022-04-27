from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L
from src.api.distributor.product_api import ProductApi

class CatalogPage(DistributorPortalPage):
    product_body = {
        "partSku": None,
        "shortDescription": None,
        "roundBuy": None,
        "lifecycleStatus": None,
        "image": None,
        "longDescription": None,
        "weight": None,
        "height": None,
        "width": None,
        "length": None,
        "issueQuantity": None,
        "packageConversion": None,
        "manufacturerPartNumber": None,
        "manufacturer": None,
        "alternative": None,
        "productLvl1": None,
        "productLvl2": None,
        "productLvl3": None,
        "attribute1": None,
        "attribute2": None,
        "attribute3": None,
        "gtin": None,
        "upc": None,
        "keyword": None,
        "unitName": None
    }

    def create_product(self, product_body):
        pa = ProductApi(self.context)
        start_number_of_rows = pa.get_products_total_elements()
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), product_body.pop("lifecycleStatus"))
        for field in product_body.keys():
            self.input_by_name(field, product_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()
        self.last_page(10)
        self.element(L.get_row_by_index(start_number_of_rows%10)).get()

    def check_last_product(self, product_body):
        table_cells = {
            "Distributor SKU": product_body["partSku"],
            "Short Description": product_body["shortDescription"],
            "Round Buy": product_body["roundBuy"],
            "Issue Quantity": product_body["issueQuantity"],
            "Package Conversion": product_body["packageConversion"],
        }
        for cell, value in table_cells.items():
            self.check_table_item(value, header=cell, last=True)

    def update_last_product(self, product_body):
        self.element(L.last_role_row+L.edit_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), product_body.pop("lifecycleStatus"))
        for field in product_body.keys():
            self.input_by_name(field, product_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def import_product(self, products):
        Tools.generate_csv("products.csv", products)
        self.import_csv(L.file_upload, "products.csv")
        self.element(L.successfully_imported_msg).get()
        self.wait_until_progress_bar_loaded()
