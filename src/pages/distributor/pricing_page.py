from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class PricingPage(DistributorPortalPage):
    pricing_body = {
        "Distributor SKU": None,
        "Price": None,
        "UOM": None,
        "Expiration Date": None
    }

    def import_pricing(self, pricing):
        Tools.generate_csv("pricing.csv", pricing)
        self.import_csv(L.file_upload, "pricing.csv")
        self.element(L.successfully_imported_msg).get()

    def check_price_by_name(self, pricing_body):
        for cell, value in pricing_body.items():
            self.check_last_table_item(cell, value)
