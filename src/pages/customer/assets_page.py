from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L
from glbl import Log

class AssetsPage(CustomerPortalPage):
    xpath_filter = "//span[text()='Filter']"
    xpath_apply = "//span[text()='Apply']"
    xpath_asset_card = "//div[@data-testid='asset-item']"
    xpath_available = "//div[text()='Available']"
    xpath_total = "//div[text()='Total']"
    xpath_checked_out = "//div[text()='Checked out']"
    xpath_user = "//div[text()='User']"
    xpath_sku_input = "//label[text()='Distributor SKU']/../div/input"
    xpath_return_requested_text = "//div[text()='Asset return has been requested']"
    #xpath_empty_list = "//div[text()='List of checked out assets is empty.']"

    def check_all_assets_tab(self, shipto, avaliable, total, checked_out):
        self.element("//span[text()='All assets']").get()
        self.click_tab_by_name("All assets")
        self.element(self.xpath_filter).click()
        self.select_in_dropdown(L.select_box, shipto)
        self.element(self.xpath_apply).click()
        self.element_should_have_text(f"{self.xpath_available}/../div[2]", f"{avaliable}")
        self.element_should_have_text(f"{self.xpath_total}/../div[2]", f"{total}")
        self.element_should_have_text(f"{self.xpath_checked_out}/../div[2]", f"{checked_out}")

    def check_checked_out_tab(self, shipto, avaliable, total, checked_out):
        self.click_tab_by_name("Checked Out")
        self.element(self.xpath_filter).click()
        self.select_in_dropdown(L.select_box, shipto)
        self.element(self.xpath_apply).click()
        if checked_out == 1:
            self.element_should_have_text(f"{self.xpath_checked_out}/../div[2]", "1 item")
        else:
            self.element_should_have_text(f"{self.xpath_checked_out}/../div[2]", f"{checked_out} items")
        self.element_should_have_text(f"{self.xpath_total}/../div[2]", f"{total}")
        self.element_should_have_text(f"{self.xpath_available}/../div[2]", f"{avaliable}")
        self.element_should_have_text(f"{self.xpath_user}/../div[2]/a", f"{self.data.customer_user_first_name} {self.data.customer_user_last_name} ({self.context.customer_email})")

    def checked_out_tab_should_not_contain(self, asset):
        self.click_tab_by_name("Checked Out")
        elements = self.element(self.xpath_asset_card).count()
        if elements == 0:
            Log.info("Checked out list is empty")
        else:
            self.element(self.xpath_filter).click()
            self.element(self.xpath_sku_input).enter(asset)
            self.element(self.xpath_apply).click()
            self.element(self.xpath_asset_card).wait_elements_number(0)

    def ping_to_return_last_asset(self):
        self.click_tab_by_name("Checked Out")
        self.element(f"{L.ping_to_return}").click()
        self.wait_until_progress_bar_loaded()
        self.element(f"({self.xpath_asset_card})[1]{self.xpath_return_requested_text}").wait_elements_number(1)
