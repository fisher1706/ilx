from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class UsageHistoryPage(DistributorPortalPage):
    usage_history_body = {
        "Order Number": None,
        "Customer Number": None,
        "ShipTo Number": None,
        "ShipTo Name": None,
        "Part SKU": None,
        "Quantity": None,
        "Date": None,
    }

    def follow_usage_history_url(self):
        self.follow_url(f"{self.url.distributor_portal}/customers/{self.data.customer_id}#usage-history")

    def import_usage_history(self, usage_history):
        Tools.generate_csv("usage_history.csv", usage_history)
        self.import_csv(L.id_file_upload, "usage_history.csv")
        self.get_element_by_xpath(L.xpath_successfully_imported_msg)
        

    def check_last_usage_history(self, usage_history_body):
        for cell, value in usage_history_body.items():
            self.check_table_item(value, header=cell, last=True)
