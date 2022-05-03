from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from glbl import Log, Error

class LockerPlanogramPage(DistributorPortalPage):
    def follow_locker_planogram_url(self, customer_id=None, shipto_id=None):
        if customer_id is None:
            customer_id = self.data.customer_id
        if shipto_id is None:
            shipto_id = self.data.shipto_id
        self.follow_url(f"{self.url.distributor_portal}/customers/{customer_id}/shiptos/{shipto_id}#planogram")

    def create_location_via_planogram(self, door, cell, sku, min_value, max_value):
        self.click_xpath(L.get_planogram(door, cell))
        self.click_xpath(L.xpath_assign_product_planogram)
        self.input_by_name("min", min_value)
        self.input_by_name("max", max_value)
        self.input_data_xpath(sku, f"{L.xpath_dialog}{L.xpath_select_box}//input")
        self.click_xpath(L.get_dropdown_sku(sku))
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()

    def open_locker_planogram(self, locker, shipto):
        self.get_element_by_xpath(L.xpath_table_row)
        locker_row = self.scan_table(scan_by=locker, column_header="Serial Number", pagination=False)
        self.click_xpath(L.xpath_by_count(L.xpath_table_row, locker_row)+L.get_planogram_button)
        self.wait_until_progress_bar_loaded()
        #check device
        text = self.get_element_text(L.get_dropdown_in_dialog(1))
        if text == f"{locker}":
            Log.info(f"Selected Device is {locker} as expected")
        else:
            Error.error(f"Selected Device is {text} but should be {locker}")
        current_url = self.driver.current_url
        result = f"{shipto}" in current_url
        if result:
            Log.info(f"URL contains shipto id {shipto}")
        else:
            Error.error(f"URL contains wrong shipto id {shipto}")

    def assign_smart_shelf_to_locker_door(self, smart_shelf):
        self.click_xpath(L.xpath_configure_button)
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), smart_shelf)
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()

    def check_smart_shelf_via_planogram(self, smart_shelf, door_number):
        self.click_xpath(L.xpath_configure_button)
        self.get_element_by_xpath(L.get_dropdown_in_dialog(2))
        self.wait_until_dropdown_not_empty(L.get_dropdown_in_dialog(2))
        text = self.get_element_text(L.get_dropdown_in_dialog(2))
        if text == "":
            for _ in range(3):
                self.click_xpath(L.xpath_close_button)
                self.click_xpath(L.xpath_configure_button)
                text = self.get_element_text(L.get_dropdown_in_dialog(2))
                if text != "":
                    break
        Log.info(f"Text in dropdown is {text}")
        assert f"{text}" == f"{smart_shelf}", f"Smart shelf {smart_shelf} is NOT assigned to the locker as expected"
        Log.info(f"Smart shelf {smart_shelf} is assigned to the locker as expected")

    def check_first_door_is_unavaliable_planogram(self):
        self.click_xpath(L.xpath_configure_button)
        self.should_be_disabled_xpath(f"{L.get_dropdown_in_dialog(2)}//input")
