import time
from src.pages.admin.admin_portal_page import AdminPortalPage
from src.resources.tools import Tools
from src.pages.locator import Locator as L
from glbl import Log, Error

class SmartShelvesPage(AdminPortalPage):
    smart_shelves_body = {
        "serialNumber": None,
        "distributor": None,
        "assign_to": None,
        "door_number": None
    }
    xpath_merge_cells = "//span[text()='MERGE CELLS']"
    xpath_split_cells = "//span[text()='SPLIT CELL']"

    def open_smart_shelves(self):
        self.sidebar_hardware()
        self.click_tab_by_name("Smart Shelves")
        self.open_last_page()

    def create_smart_shelves(self, smart_shelves_body):
        self.element(L.add_button).click()
        # input Serial Number
        self.input_by_name("serialNumber", smart_shelves_body["serialNumber"])
        # input Distributor and check if Assign To is editable
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), smart_shelves_body["distributor"])
        self.element(L.get_dropdown_in_dialog(2)).wait_until_enabled()
        # input Assign To and check if Door Number is editable
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), smart_shelves_body["assign_to"])
        self.element(L.get_dropdown_in_dialog(3)).wait_until_enabled()
        # input Door Number
        self.select_in_dropdown(L.get_dropdown_in_dialog(3), smart_shelves_body["door_number"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def check_last_smart_shelf(self, smart_shelves_body):
        table_cells = {
            "Serial Number": smart_shelves_body["serialNumber"],
            "Assigned Device": smart_shelves_body["assign_to"],
            "Distributor": smart_shelves_body["distributor"],
            "Qnty of Cells": "4"
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_by_header(cell, value)

    def update_smart_shelves(self, smart_shelves_body):
        self.element(L.last_role_row + L.edit_button).click()
        # input Serial Number
        self.input_by_name("serialNumber", smart_shelves_body["serialNumber"])
        # change Distributor and check if fields "Assign To" and "Door Number" become empty
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), smart_shelves_body["distributor"])
        self.element(f"{L.get_dropdown_in_dialog(3)}//input").wait_until_disabled()
        text = self.element(L.get_dropdown_in_dialog(2)).text()
        assert text is None or text == "", f"Element {L.get_dropdown_in_dialog(2)} contains text: {text}"
        # input Assign To and check if Door Number is editable
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), smart_shelves_body["assign_to"])
        self.element(L.get_dropdown_in_dialog(3)).wait_until_enabled()
        # input Door Number
        time.sleep(3)#need to use wait
        self.select_in_dropdown(L.get_dropdown_in_dialog(3), smart_shelves_body["door_number"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def delete_smart_shelf(self, serial_number):
        self.get_last_table_item_text_by_header("Serial Number")
        self.element(L.last_role_row + L.remove_button).click()
        self.delete_dialog_should_be_about(f"{serial_number}")
        self.element(L.confirm_button).click()
        self.dialog_should_not_be_visible()

    def merge_cells(self, number_of_cells):
        self.element(L.last_role_row + L.edit_button).click()
        for cell in range(number_of_cells):
            self.element(f"//div[@data-cell='{cell}']").click()
        self.element(self.xpath_merge_cells).click()
        self.element(L.submit_button).click()
        self.element(L.label_confirm).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def split_cells(self, position_of_cell):
        self.element(L.last_role_row + L.edit_button).click()
        self.element(f"//div[@data-cell='{position_of_cell}']").click()
        self.element(self.xpath_split_cells).click()
        self.element(L.submit_button).click()
        self.element(L.label_confirm).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def check_cells_number(self, number_of_cells):
        self.element(L.table_row).get()
        self.check_last_table_item_by_header("Qnty of Cells", "4")
        self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
        self.element("//div[@data-cell]").wait_elements_number(number_of_cells)
        self.element(L.label_cancel).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def check_first_door_is_unavaliable(self, locker, create=None):
        if create is None:
            self.element(L.last_role_row + L.edit_button).click()
        elif create:
            self.element(L.add_button).click()
            # input Serial Number
            self.input_by_name("serialNumber", Tools.random_string_u())
            # input Distributor
            self.select_in_dropdown(L.get_dropdown_in_dialog(1), self.data.distributor_name)
        # input Assign To
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), locker)
        # check Door Number
        self.element(L.get_dropdown_in_dialog(3)).click()
        time.sleep(3)#need to use wait
        text = self.element(f"{L.dropdown_list_item}/div").text()
        if f"{text}" == "2":
            Log.info("First door is unavailable as expected")
        else:
            Error.error("First door shoud not be avaliable")
        self.element(L.get_dropdown_in_dialog(3)).click()
        self.element(L.label_cancel).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def clear_fields_smart_shelves(self, distributor=None, locker=None):
        self.element(L.last_role_row + L.edit_button).click()
        self.element_should_have_text(L.get_dropdown_in_dialog(3), "1")
        if locker is not None:
            self.element(f"{L.get_dropdown_in_dialog(2)}/div/div[2]/div").click()
        if distributor is not None:
            self.element(f"{L.get_dropdown_in_dialog(1)}/div/div[2]/div").click()
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def assign_smart_shelf_locker_planogram(self, locker, smart_shelf):
        self.element(L.table_row).get()
        self.open_last_page()
        self.element(L.table_row).get()
        locker_row = self.get_row_of_table_item_by_header(locker, "Serial Number")
        self.element(L.get_indexed(L.table_row, locker_row)+L.planogram_button).click()
        self.element(L.configure_button).click()
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), smart_shelf)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()

    def check_smart_shelf_unavailable_via_planogram(self, locker, smart_shelf, in_list=False):
        self.open_last_page()
        self.element(L.last_role_row + L.planogram_button).click()
        self.element(L.configure_button).click()
        self.element(L.get_dropdown_in_dialog(1)).click()
        self.element(f"{L.get_dropdown_in_dialog(1)}//input").enter(smart_shelf)
        text = self.element(f"{L.dropdown_list_item}/div").text()
        if in_list:
            if f"{text}" == f"{smart_shelf}":
                Log.info(f"There is {smart_shelf} as expected")
            else:
                Error.error(f"Smart Shelf {smart_shelf} should be in the list")
        else:
            if f"{text}" == f"{smart_shelf}":
                Error.error(f"Smart Shelf {smart_shelf} should not be in the list")
            else:
                Log.info(f"There is no {smart_shelf} as expected")
        self.element(L.close_button).click()
        self.dialog_should_not_be_visible()
