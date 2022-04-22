from selenium.webdriver.common.keys import Keys
from glbl import LOG
from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.resources.locator import Locator
from src.api.customer.customer_user_api import CustomerUserApi

class AllocationCodesPage(CustomerPortalPage):
    allocation_code_body = {
        "name": None,
        "type": None,
        "values": None,
        "isRequired": None
        # "shiptos": None
    }
    xpath_add_to_list = "//span[text()='Add to list']"

    def add_allocation_code(self, allocation_code_body):
        ca = CustomerUserApi(self.context)
        allocation_codes_count = len(ca.get_allocation_codes())
        self.click_id(Locator.id_add_button)
        self.select_in_dropdown(Locator.xpath_dropdown_in_dialog(1), allocation_code_body.pop("type"))
        self.set_slider(Locator.xpath_checkbox, allocation_code_body.pop("isRequired"))
        self.enter_values(allocation_code_body.pop("values"))
        for field in allocation_code_body.keys():
            self.input_by_name(field, allocation_code_body[field])
        self.click_xpath(self.xpath_add_to_list)
        self.click_xpath(Locator.xpath_submit_button)
        self.click_xpath(Locator.xpath_reload_button)
        self.element_should_have_text(Locator.xpath_get_table_item_by_index(allocation_codes_count, 1), allocation_code_body["name"])
        self.click_xpath(Locator.xpath_last_role_row + Locator.xpath_info_button)

    def enter_values(self, values):
        if values is not None:
            for value in values:
                element = self.get_element_by_xpath("//label[text()='Values']/..//input")
                element.send_keys(value)
                element.send_keys(Keys.ENTER)

    def check_allocation_code(self, allocation_code_body):
        table_cells = {
            "Name": allocation_code_body["name"],
            "Type": allocation_code_body["type"],
            "Values": allocation_code_body["values"],
        }
        for cell, value in table_cells.items():
            self.check_table_item_by_header(self.get_row_of_table_item_by_header(table_cells["Name"], "Name"), cell, value)

    def update_allocation_code(self, current_name, allocation_code_body):
        self.click_xpath(Locator.xpath_by_count(Locator.xpath_table_row, self.get_row_of_table_item_by_header(current_name, "Name")))
        self.set_slider(Locator.xpath_checkbox, allocation_code_body.pop("isRequired"))
        self.manage_shipto(allocation_code_body.pop("shiptos"))
        self.enter_values(allocation_code_body.pop("values"))
        for field in allocation_code_body.keys():
            self.input_by_name(field, allocation_code_body[field])
        self.click_xpath(self.xpath_add_to_list)
        self.click_xpath(Locator.xpath_submit_button)

    def delete_allocation_code(self, current_name):
        current_element_row = self.get_row_of_table_item_by_header(current_name, "Name")
        name = self.get_table_item_text_by_header("Name", current_element_row)
        self.click_xpath(Locator.xpath_by_count(Locator.xpath_remove_button, current_element_row))
        self.delete_dialog_should_be_about(name)
        self.click_xpath(Locator.xpath_submit_button)
        self.dialog_should_not_be_visible()
        self.wait_until_page_loaded()
