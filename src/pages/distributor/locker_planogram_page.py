from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from glbl import Log, Error

class LockerPlanogramPage(DistributorPortalPage):
    xpath_assign_product_planogram = "//button[@type='button']/span[text()='ASSIGN PRODUCT']"
    def follow_locker_planogram_url(self, customer_id=None, shipto_id=None):
        if customer_id is None:
            customer_id = self.data.customer_id
        if shipto_id is None:
            shipto_id = self.data.shipto_id
        self.follow_url(f"{self.url.distributor_portal}/customers/{customer_id}/shiptos/{shipto_id}#planogram")
        self.wait_until_progress_bar_loaded(get_timeout=10)
        self.wait_until_progress_bar_loaded(get_timeout=5)

    def create_location_via_planogram(self, door, cell, sku, min_value, max_value):
        self.element(L.get_planogram(door, cell)).click()
        self.element(self.xpath_assign_product_planogram).click()
        self.input_by_name("min", min_value)
        self.input_by_name("max", max_value)
        self.element(f"{L.dialog}{L.select_box}//input").enter(sku)
        self.element(L.get_dropdown_sku(sku)).click()
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def open_locker_planogram(self, locker, shipto):
        self.element(L.table_row).get()
        self.element(L.last_role_row + L.planogram_button).click()
        self.wait_until_progress_bar_loaded()
        #check device
        text = self.element(L.get_dropdown_in_dialog(1)).text()
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
        self.element(L.configure_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), smart_shelf)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def check_smart_shelf_via_planogram(self, smart_shelf):
        self.element(L.configure_button).click()
        self.element(L.get_dropdown_in_dialog(2)).get()
        self.wait_until_dropdown_not_empty(L.get_dropdown_in_dialog(2))
        text = self.element(L.get_dropdown_in_dialog(2)).text()
        if text == "":
            for _ in range(3):
                self.element(L.close_button).click()
                self.element(L.configure_button).click()
                text = self.element(L.get_dropdown_in_dialog(2)).text()
                if text != "":
                    break
        Log.info(f"Text in dropdown is {text}")
        assert f"{text}" == f"{smart_shelf}", f"Smart shelf {smart_shelf} is NOT assigned to the locker as expected"
        Log.info(f"Smart shelf {smart_shelf} is assigned to the locker as expected")

    def check_first_door_is_unavaliable_planogram(self):
        self.element(L.configure_button).click()
        self.element(f"{L.get_dropdown_in_dialog(2)}//input").wait_until_disabled()
