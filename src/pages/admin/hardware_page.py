import random
from src.pages.admin.admin_portal_page import AdminPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L

class HardwarePage(AdminPortalPage):
    xpath_weight_radio = "//input[@name='noWeight' and @type='radio' and @value='false']"
    xpath_no_weight_radio = "//input[@name='noWeight' and @type='radio' and @value='true']"
    xpath_door_serial_number_title = "//div[text()='Door Serial Number']"
    xpath_door_serial_number = f"{xpath_door_serial_number_title}/../div[2]"
    xpath_smart_shelf_absence_title = "//span[text()='There is no smart shelf assigned']"

    def create_iothub(self, distributor):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), "IoT Hub")
        self.element(L.get_dropdown_in_dialog(7)).get()
        self.select_in_dropdown(L.get_dropdown_in_dialog(7), distributor)
        self.element(L.submit_button).click()
        self.wait_until_progress_bar_loaded()
        self.element("//h6[text()='IoTHub provision information']").get()
        self.element("//div[text()='Access Key:']/../span").get()
        serial_number = self.element("//div[text()='Access Key:']/../span").text()
        self.element(L.close_button).click()
        self.dialog_should_not_be_visible()
        return serial_number

    #need to replace the args with dict and rempve pylint comment
    def check_last_hardware(self, serial_number=None, device_type=None, iothub=None, device_name=None, distributor=None, customer_shipto=None, distributor_user=None, customer_user=None, expiration_date=None, device_subtype=None): #pylint: disable=C0301, R0913
        self.open_last_page()
        self.check_last_table_item_outdated("Serial Number", serial_number)
        self.check_last_table_item_outdated("Device Type", device_type)
        self.check_last_table_item_outdated("IoT Hub", iothub)
        self.check_last_table_item_outdated("Device name", device_name)
        self.check_last_table_item_outdated("Distributor", distributor)
        self.check_last_table_item_outdated("Customer-ShipTo", customer_shipto)
        self.check_last_table_item_outdated("Distributor User", distributor_user)
        self.check_last_table_item_outdated("Customer User", customer_user)
        self.check_last_table_item_outdated("Expiration Date", expiration_date)
        self.check_last_table_item_outdated("Device Sub-Type", device_subtype)

    def update_last_iothub(self, distributor):
        self.open_last_page()
        self.element(L.last_role_row + L.edit_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(8), distributor)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def remove_last_hardware(self, serial_number=None):
        self.open_last_page()
        self.element(L.last_role_row + L.remove_button).click()
        if serial_number is not None:
            self.delete_dialog_should_be_about(serial_number)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def iothub_should_be_available(self, type_name, hub_text, inverse=False):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), type_name)
        self.element(L.get_dropdown_in_dialog(6)).click()
        element = self.element(L.dropdown_list_item + f"/div[text()='{hub_text}']")
        if inverse:
            element.wait_for_not_appeared(3)
        else:
            element.get()
        self.element(L.close_button).click()

    def create_locker(self, iothub_name):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), "Locker")
        self.select_in_dropdown(L.get_dropdown_in_dialog(6), iothub_name)
        self.select_in_dropdown(L.get_dropdown_in_dialog(8), "Standard")
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def create_vending(self, iothub_name):
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), "Vending")
        self.select_in_dropdown(L.get_dropdown_in_dialog(6), iothub_name)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def configure_locker_door(self, door_number=None, serial_number=None, is_weight=False):
        self.element(L.last_role_row + L.planogram_button).click()
        self.element(L.configure_button).get()
        if door_number is None:
            count = self.element(L.configure_button).count()
            door_number = random.choice(range(count))+1
        if serial_number is None:
            serial_number = Tools.random_string_u()
        self.element(L.get_indexed(L.configure_button, door_number)).click()
        if not is_weight:
            xpath_radio = self.xpath_no_weight_radio
        else:
            xpath_radio = self.xpath_weight_radio
        self.element(f"{xpath_radio}/../..").click()
        self.input_by_name("doorSerial", serial_number)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        data = {
            "doors_count": count,
            "door": door_number,
            "weight": is_weight,
            "serial_number": serial_number
        }
        return data

    def check_locker_door(self, doors_data):
        assert doors_data["serial_number"] == self.element(self.xpath_door_serial_number).text(), "The Door SN is incorrect"
        if not doors_data["weight"]:
            smart_shelves = self.element(self.xpath_smart_shelf_absence_title).count()
            assert doors_data["doors_count"] == smart_shelves + 1, "The number of noWeight doors is incorrect"
