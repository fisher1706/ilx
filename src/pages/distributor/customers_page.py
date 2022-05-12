from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
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
    button_next = "//button/span[text()='Next']"

    def create_customer(self, customer_body):
        self.element(L.item_action_customer_add).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(3), customer_body.pop("warehouse"))
        self.set_slider(L.dialog+L.checkbox, customer_body.pop("supplyForce"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.last_page(10)
        self.check_last_table_item("Name", customer_body["name"])

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
        self.element(L.last_role_row+L.customer_info_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        self.set_slider(L.checkbox, customer_body.pop("supplyForce"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.element(L.submit_button).click()

    def click_on_customer_setup_wizard_button(self):
        self.element("//button/span[text()='Customer setup wizard']").click()

    def check_customer_setup_wizard_button(self):
        if self.element("//button/span[text()='Customer setup wizard']").count() == 0:
            Log.info("Button is hidden for user")
        else:
            Error.error("Create setup wizard button is enabled for user")

    def select_warehouse(self):
        self.element(f"{L.get_table_item(1, 5)}//button").click()
        self.element(self.button_next).click()

    def add_customer_info(self, customer_body):
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), customer_body.pop("customerType"))
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), customer_body.pop("marketType"))
        for field in customer_body.keys():
            self.input_by_name(field, customer_body[field])
        self.element(self.button_next).click()

    def add_customer_portal_user(self, email):
        self.select_checkbox(L.checkbox)
        self.element("//input[@value='']").enter(email)

    def click_complete(self):
        self.element(L.complete_button).click()

    def click_next(self):
        self.element(self.button_next).click()

    def check_customer_portal_user(self, expected_email):
        table_cells = {
            "Email": expected_email
        }
        for cell, value in table_cells.items():
            self.check_last_table_item(cell, value)

    def check_settings_reorder_list_settings(self, expected_email):
        self.element("//span[text()='Reorder List Settings']").click()
        assert self.element("//input[@name='email']").get().get_attribute("value") == expected_email

    def change_automation_settings(self, email):
        self.element("//span[text()='Use Defaults']").click()
        self.element("//input[@name='email']").enter(email)
        self.element("//span[text()='Submit Immediately']").click()
        self.element("//span[text()='Auto-submit as ORDER']").click()
        self.element(L.complete_button).click()

    def delete_last_customer(self, value):
        self.element(L.last_role_row+L.remove_button).click()
        self.delete_dialog_should_be_about(value)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
