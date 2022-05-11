from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.api.distributor.customer_api import CustomerApi
from glbl import Log, Error

class CustomersPage(DistributorPortalPage):
    customer_body = {
        "name": None,
        "number": None,
        "customerType": None,
        "marketType": None,
        "warehouse": None,
        "notes": None,
        "supplyForce": None
    }

    def create_customer(self, customer_body):
        ca = CustomerApi(self.context)
        start_number_of_rows = ca.get_customers(full=True)["totalElements"]
        self.click_id(L.id_item_action_customer_add)
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(3), customer_body.pop("warehouse"))
        self.set_slider(L.xpath_dialog+L.xpath_checkbox, customer_body.pop("supplyForce"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()
        self.last_page(10)
        self.get_element_by_xpath(L.get_row_by_index(start_number_of_rows%10))

    def check_last_customer(self, customer_body):
        table_cells = {
            "Name": customer_body["name"],
            "Number": customer_body["number"],
            "Warehouse": customer_body["warehouse"],
            "Customer Type": customer_body["customerType"],
            "Market Type": customer_body["marketType"]
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def update_last_customer(self, customer_body):
        self.click_xpath(L.xpath_last_role_row+L.xpath_customer_info_button)
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        self.set_slider(L.xpath_checkbox, customer_body.pop("supplyForce"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.click_xpath(L.xpath_submit_button)

    def click_on_customer_setup_wizard_button(self):
        self.click_xpath("//button/span[text()='Customer setup wizard']")

    def check_customer_setup_wizard_button(self):
        
        if self.get_element_count("//button/span[text()='Customer setup wizard']") == 0:
            Log.info("Button is hidden for user")
        else:
            Error.error("Create setup wizard button is enabled for user")

    def select_warehouse(self):
        self.click_xpath(f"{L.xpath_table_item(1, 5)}//button")
        self.click_xpath(L.xpath_next)

    def add_customer_info(self, customer_body):
        
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.click_xpath(L.xpath_next)

    def add_customer_portal_user(self, email):
        
        self.select_checkbox(L.xpath_checkbox)
        self.get_element_by_xpath("//input[@value='']").send_keys(email)

    def click_complete(self):
        self.click_xpath(L.xpath_complete_button)
        

    def click_next(self):
        self.click_xpath(L.xpath_next)
        

    def check_customer_portal_user(self, expected_email):
        
        table_cells = {
            "Email": expected_email
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def check_settings_reorder_list_settings(self, expected_email):
        
        self.click_xpath("//span[text()='Reorder List Settings']")
        assert self.get_element_by_xpath("//input[@name='email']").get_attribute("value") == expected_email

    def change_rows_per_page(self):
        ca = CustomerApi(self.context)
        start_number_of_rows = ca.get_customers(full=True)["totalElements"]
        self.last_page(10)
        self.get_element_by_xpath(L.get_row_by_index(start_number_of_rows%10))
        

    def change_automation_settings(self, email):
        
        self.click_xpath("//span[text()='Use Defaults']")
        self.clear_xpath("//input[@name='email']")
        self.get_element_by_xpath("//input[@name='email']").send_keys(email)
        self.click_xpath("//span[text()='Submit Immediately']")
        self.click_xpath("//span[text()='Auto-submit as ORDER']")
        self.click_xpath(L.xpath_complete_button)
        

    def delete_last_customer(self, value):
        self.click_xpath(L.xpath_last_role_row+L.xpath_remove_button)
        self.delete_dialog_should_be_about(value)
        self.click_xpath(L.xpath_submit_button)
        self.dialog_should_not_be_visible()
