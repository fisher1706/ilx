from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class OrderStatusPage(DistributorPortalPage):
    def update_transaction(self, row, reorder_quantity=None, shipped_quantity=None, status=None):
        if (reorder_quantity is not None or status is not None):
            self.click_xpath(L.xpath_by_count(L.xpath_edit_button, row))
            if reorder_quantity is not None:
                self.input_by_name("reorderQuantity", reorder_quantity)
            if status is not None:
                self.select_in_dropdown(L.get_dropdown_in_dialog(1), status)
            if shipped_quantity is not None:
                self.input_by_name("shippedQuantity", shipped_quantity)
            self.click_xpath(L.xpath_submit_button)
            self.dialog_should_not_be_visible()
            

    def split_transaction(self, row, quantity):
        self.click_xpath(L.xpath_by_count(L.xpath_split_button, row))
        self.input_by_name("splitFrom", quantity)
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()
        
