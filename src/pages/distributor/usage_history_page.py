from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class UsageHistoryPage(DistributorPortalPage):
    usage_history_body = {
        "Order Number": None,
        "Customer Number": None,
        "ShipTo Number": None,
        "ShipTo Name": None,
        "Distributor SKU": None,
        "Quantity": None,
        "Date": None,
    }

    def follow_usage_history_url(self):
        self.follow_url(f"{self.url.distributor_portal}/customers/{self.data.customer_id}#usage-history")

    def import_usage_history(self, usage_history):
        Tools.generate_csv("usage_history.csv", usage_history)
        self.import_csv(L.file_upload, "usage_history.csv")
        self.element(L.successfully_imported_msg).get()

    def check_last_usage_history(self, usage_history_body):
        for cell, value in usage_history_body.items():
            self.check_last_table_item(cell, value)
