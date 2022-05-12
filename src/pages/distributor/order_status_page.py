from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class OrderStatusPage(DistributorPortalPage):
    def update_transaction(self, reorder_quantity=None, shipped_quantity=None, status=None):
        if (reorder_quantity is not None or status is not None):
            self.element(L.last_role_row + L.edit_button).click()
            if reorder_quantity is not None:
                self.input_by_name("reorderQuantity", reorder_quantity)
            if status is not None:
                self.select_in_dropdown(L.get_dropdown_in_dialog(1), status)
            if shipped_quantity is not None:
                self.input_by_name("shippedQuantity", shipped_quantity)
            self.element(L.submit_button).click()
            self.dialog_should_not_be_visible()

    def split_transaction(self, quantity):
        self.element(L.last_role_row + L.split_button).click()
        self.input_by_name("splitFrom", quantity)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
