from src.pages.admin.admin_portal_page import AdminPortalPage
import time
import random

class HardwarePage(AdminPortalPage):
    def __init__(self, activity):
        super().__init__(activity)

    def create_iothub(self, distributor):
        self.click_xpath(self.locators.class_button_info)
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 1), "IoT Hub")
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 2), distributor)
        self.click_xpath(self.locators.class_button_ok)
        self.should_be_present_xpath("//h4[text()='IoT HUB provision information']")
        serial_number = self.get_element_text(self.locators.class_modal_dialog+self.locators.class_jumbotron+"/h3")
        self.click_xpath(self.locators.class_button_close)
        self.dialog_should_not_be_visible()
        return serial_number

    def check_last_hardware(self, serial_number=None, device_type=None, iothub=None, device_name=None, distributor=None, customer_shipto=None, distributor_user=None, customer_user=None, expiration_date=None, device_subtype=None):
        self.open_last_page_bootstrap()
        self.check_last_table_item_by_header_bootstrap("Serial Number", serial_number)
        self.check_last_table_item_by_header_bootstrap("Device Type", device_type)
        self.check_last_table_item_by_header_bootstrap("IoT Hub", iothub)
        self.check_last_table_item_by_header_bootstrap("Device name", device_name)
        self.check_last_table_item_by_header_bootstrap("Distributor", distributor)
        self.check_last_table_item_by_header_bootstrap("Customer-ShipTo", customer_shipto)
        self.check_last_table_item_by_header_bootstrap("Distributor User", distributor_user)
        self.check_last_table_item_by_header_bootstrap("Customer User", customer_user)
        self.check_last_table_item_by_header_bootstrap("Expiration Date", expiration_date)
        self.check_last_table_item_by_header_bootstrap("Device Sub-Type", device_subtype)

    def update_last_iothub(self, distributor):
        self.open_last_page_bootstrap()
        self.click_xpath(self.locators.xpath_by_count(self.locators.class_button_success, self.get_table_rows_number_bootstrap()))
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 1), distributor)
        self.click_xpath(self.locators.class_button_ok)
        self.dialog_should_not_be_visible()

    def remove_last_hardware(self):
        self.open_last_page_bootstrap()
        self.click_xpath(self.locators.xpath_by_count(self.locators.class_button_danger, self.get_table_rows_number_bootstrap()))
        self.click_xpath("//span[text()='Yes, delete item']/..")
        self.dialog_should_not_be_visible()

    def is_iothub_available_in_dialog(self, type_name, hub_text):
        result = False
        self.click_xpath(self.locators.class_button_info)
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 1), type_name)
        self.click_xpath(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 2))
        dropdown_list_item_xpath = "//div[text()='-- select a IoTHub --']/../div"
        number_of_dropdown_list_items = self.get_element_count(dropdown_list_item_xpath)
        for index in range(1, number_of_dropdown_list_items+1):
            dropdown_list_item_text = self.get_element_text(self.locators.xpath_by_count(dropdown_list_item_xpath, index))
            if (dropdown_list_item_text == hub_text):
                result = True
                break
        else:
            result = False
        self.click_xpath(self.locators.class_button_close)
        return result

    def iothub_should_be_available(self, type_name, hub_text):
        if (self.is_iothub_available_in_dialog(type_name, hub_text)):
            self.logger.info("IoT Hub '"+hub_text+"' is found")
        else:
            self.logger.error("IoT Hub '"+hub_text+"' is not found")

    def iothub_should_not_be_available(self, type_name, hub_text):
        if (not self.is_iothub_available_in_dialog(type_name, hub_text)):
            self.logger.info("There is no IoT Hub '"+hub_text+"'")
        else:
            self.logger.error("There is IoT Hub '"+hub_text+"', but it should NOT be here")

    def create_locker(self, distributor, iothub_name):
        self.click_xpath(self.locators.class_button_info)
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 1), "Locker")
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 2), iothub_name)
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 3), "Standard")
        self.click_xpath(self.locators.class_button_ok)
        self.dialog_should_not_be_visible()

    def create_vending(self, distributor, iothub_name):
        self.click_xpath(self.locators.class_button_info)
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 1), "Vending")
        self.select_in_dropdown(self.locators.xpath_by_count(self.locators.bootstrap_select_box, 2), iothub_name)
        self.click_xpath(self.locators.class_button_ok)
        self.dialog_should_not_be_visible()

    def configure_last_locker_door(self, clear_previous_data=None):
        self.click_xpath(self.locators.xpath_by_count(self.locators.bootstrap_table_row, self.get_table_rows_number_bootstrap())+self.locators.class_button_default)
        if (clear_previous_data is not None):
            self.unselect_checkbox(self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_checkbox, clear_previous_data["checkbox"]))
            self.clear_xpath(self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_type_text, clear_previous_data["text"]))
        count = self.get_element_count(self.locators.xpath_dialog+self.locators.xpath_checkbox)
        checking_count = self.get_element_count(self.locators.xpath_dialog+self.locators.xpath_type_text)
        assert count == checking_count, "The number of checkboxes should be equal to the number of text fields"
        if (count > 1):
            checkbox = random.choice(range(1, count))
            text_field = random.choice(range(1, count))
        else:
            checkbox = 1
            text_field = 1
        self.select_checkbox(self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_checkbox, checkbox))
        self.input_data_xpath(str(text_field), self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_type_text, text_field))
        self.click_xpath(self.locators.xpath_confirm_button)
        self.dialog_should_not_be_visible()
        data = {
            "checkbox": checkbox,
            "text": text_field
        }
        return data

    def check_last_locker_door(self, doors_data):
        self.click_xpath(self.locators.xpath_by_count(self.locators.bootstrap_table_row, self.get_table_rows_number_bootstrap())+self.locators.class_button_default)
        self.checkbox_should_be(self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_checkbox, doors_data["checkbox"]), True)
        if (self.get_element_xpath(self.locators.xpath_by_count(self.locators.xpath_dialog+self.locators.xpath_type_text, doors_data["text"])).get_attribute("value") != str(doors_data["text"])):
            self.logger.error("There is no necessary value in the '"+str(doors_data["text"])+"' text field")
        else:
            self.logger.info("Value in the '"+str(doors_data["text"])+"' text field is correct")
        self.click_xpath(self.locators.xpath_dialog+self.locators.xpath_dialog_cancel_button)
        self.dialog_should_not_be_visible()