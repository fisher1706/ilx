from src.pages.admin.admin_portal_page import AdminPortalPage
from src.pages.locator import Locator as L

class FeesPage(AdminPortalPage):
    fee_price = {
        "Level 1": None,
        "Level 2": None,
        "Level 3": None
    }

    def set_fee_price(self, fee_price):
        self.click_tab_by_name("ShipTo Fees")
        for row, field in enumerate(fee_price.keys()):
            self.input_inline_xpath(fee_price[field], f"{L.get_table_item_outdated(row+1, 2)}")
            self.wait_until_progress_bar_loaded()

    def check_fee_price(self, fee_price):
        self.page_refresh()
        for row, field in enumerate(fee_price.keys()):
            self.check_table_item_outdated(row+1, "Price", f"${fee_price[field]}.00")

    def undo(self, fee_price):
        for _ in fee_price.keys():
            self.element(L.action_button).click()
            self.wait_until_progress_bar_loaded()
