from selenium.webdriver.common.keys import Keys
from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L
from src.api.customer.customer_user_api import CustomerUserApi

class AllocationCodesPage(CustomerPortalPage):
    allocation_code_body = {
        "name": None,
        "type": None,
        "values": None,
        "isRequired": None
    }
    xpath_add_to_list = "//span[text()='Add to list']"
    xpath_associate_table_row = "//table/tbody/tr"
    xpath_associate_table_column = "//td"

    def add_allocation_code(self, allocation_code_body):
        ca = CustomerUserApi(self.context)
        allocation_codes_count = len(ca.get_allocation_codes())
        self.element(L.add_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), allocation_code_body.pop("type"))
        self.set_slider(L.get_indexed(L.checkbox, 1), allocation_code_body.pop("isRequired"))
        self.enter_values(allocation_code_body.pop("values"))
        for field in allocation_code_body.keys():
            self.input_by_name(field, allocation_code_body[field])
        self.element(self.xpath_add_to_list).click()
        self.element_should_have_text(L.get_table_item_by_index(allocation_codes_count, 1), allocation_code_body["name"])

    def enter_values(self, values):
        if values is not None:
            for value in values:
                element = self.element("//label[text()='Values']/..//input").get()
                element.send_keys(value)
                element.send_keys(Keys.ENTER)

    def check_allocation_code(self, allocation_code_body):
        table_cells = {
            "Name": allocation_code_body["name"],
            "Type": allocation_code_body["type"],
            "Values": allocation_code_body["values"],
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)
        if allocation_code_body["isRequired"] == "true":
            self.element("(//div[@role='row'])[last()]//div[@role='cell'][4]//*[name()='svg']").get()

    def get_element_xpath_in_associate_table(self, row, column):
        return f"(({self.xpath_associate_table_row})[{row}]{self.xpath_associate_table_column})[{column}]"

    def get_element_text_in_associate_table(self, row, column):
        element_xpath = self.get_element_xpath_in_associate_table(row, column)
        return self.element(element_xpath).text()

    def get_associate_subsite_row(self, subsite_name, subsite_number):
        subsite_number = str(subsite_number).upper()
        subsite_text = f"{subsite_name} " + f"({subsite_number})"
        self.element(self.xpath_associate_table_row).get()
        rows_count = self.element(self.xpath_associate_table_row).count()
        for index in range(1, rows_count + 1):
            element_text = self.get_element_text_in_associate_table(index, 1)
            if element_text == subsite_text:
                return index

    def associate_subsite_with_allocation_code(self, subsite_name, subsite_number):
        self.element(L.last_role_row + L.info_button).click()
        row = self.get_associate_subsite_row(subsite_name, subsite_number)
        self.select_checkbox(self.get_element_xpath_in_associate_table(row, 3) + L.xpath_checkbox)
        self.element(L.get_indexed(L.submit_button, 2)).click()
        self.element("//a[@href='/customer/allocation-codes']").click()

    def check_associated(self, subsite_name, subsite_number, shipto_name_1, shipto_number_1, shipto_name_2, shipto_number_2, checked=None):
        shipto_text_1 = f"{shipto_name_1} " + f"({shipto_number_1})"
        shipto_text_2 = f"{shipto_name_2} " + f"({shipto_number_2})"
        self.element(L.last_role_row + L.info_button).click()
        row = self.get_associate_subsite_row(subsite_name, subsite_number)
        self.element(self.get_element_xpath_in_associate_table(row,1) + "//button").click()
        self.element_should_have_text(self.get_element_xpath_in_associate_table(row + 1, 1), shipto_text_1)
        self.element_should_have_text(self.get_element_xpath_in_associate_table(row + 2, 1), shipto_text_2)
        for row_index in range(row, row + 3):
            if checked:
                self.checkbox_should_be(self.get_element_xpath_in_associate_table(row_index, 3) + L.checkbox, True)
            else:
                self.checkbox_should_be(self.get_element_xpath_in_associate_table(row_index, 3) + L.checkbox, False)
        self.element("//a[@href='/customer/allocation-codes']").click()

    def update_associated(self, subsite_name, subsite_number):
        self.element(L.last_role_row + L.info_button).click()
        row = self.get_associate_subsite_row(subsite_name, subsite_number)
        self.element(self.get_element_xpath_in_associate_table(row, 1) + "//button").click()
        for row_index in range(row + 1, row + 3):
            self.unselect_checkbox(self.get_element_xpath_in_associate_table(row_index, 3) + L.checkbox)
        self.element(L.get_indexed(L.submit_button, 2)).click()
        self.element("//a[@href='/customer/allocation-codes']").click()

    def update_allocation_code(self, allocation_code_body):
        self.element(L.last_role_row + L.info_button).click()
        self.set_slider(L.get_indexed(L.checkbox, 1), allocation_code_body.pop("isRequired"))
        self.enter_values(allocation_code_body.pop("values"))
        for field in allocation_code_body.keys():
            self.input_by_name(field, allocation_code_body[field])
        self.element(self.xpath_add_to_list).click()
        self.element(L.submit_button).click()
        self.element("//a[@href='/customer/allocation-codes']").click()
        self.element_should_have_text(L.last_role_row, allocation_code_body["name"])

    def delete_allocation_code(self, allocation_code_body):
        self.element(L.last_role_row + L.remove_button).click()
        self.delete_dialog_should_be_about(allocation_code_body["name"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
