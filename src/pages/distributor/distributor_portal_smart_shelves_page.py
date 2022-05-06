from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L

class DistributorSmartShelvesPage(DistributorPortalPage):
    smart_shelves_body = {
        "assign_to": None,
        "door_number": None
    }
    xpath_merge_cells = "//span[text()='MERGE CELLS']"
    xpath_split_cells = "//span[text()='SPLIT CELL']"

    def open_smart_shelves(self):
        self.sidebar_hardware()
        self.click_tab_by_name("Smart shelves")

    def update_smart_shelves(self, smart_shelves_body):
        self.open_last_page()
        self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
        self.element("//input[@name='serialNumber']").wait_until_disabled()
        self.element("//input[@name='cellsQuantity']").wait_until_disabled()
        self.element(f"{L.get_dropdown_in_dialog(2)}//input").wait_until_disabled()
        # input Assign To and check if Door Number is editable
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), smart_shelves_body["assign_to"])
        self.element(L.get_dropdown_in_dialog(2)).wait_until_enabled()
        # input Door Number
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), smart_shelves_body["door_number"])
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()

    def check_last_smart_shelf(self, smart_shelves_body):
        table_cells = {
            "Serial Number": smart_shelves_body["serialNumber"],
            "Assigned Device Name": smart_shelves_body["assign_to"],
            "Qnty of Cells": "4"
        }
        for cell, value in table_cells.items():
            self.check_last_table_item_by_header(cell, value)

    def merge_cells(self, number_of_cells, is_planogram=False, door_number=None):
        if not is_planogram:
            self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
            for cell in range(number_of_cells):
                self.element(f"//div[@data-cell='{cell}']").click()
            self.element(self.xpath_merge_cells).click()
            self.element(L.submit_button).click()
            self.element(L.label_confirm).click()
            self.dialog_should_not_be_visible()
            self.wait_until_progress_bar_loaded()
        else:
            for cell in range(1, number_of_cells + 1):
                self.element(f"//div[@data-door={door_number}]//div[@data-cell='{cell}']").click()
            self.element(self.xpath_merge_cells).click()
            self.element(f"//div[@data-door={door_number}]//div[@data-cell='1']").click()

    def split_cells(self, position_of_cell, is_planogram=False, door_number=None):
        if not is_planogram:
            self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
            self.element(f"//div[@data-cell='{position_of_cell}']").click()
            self.element(self.xpath_split_cells).click()
            self.element(L.submit_button).click()
            self.element(L.label_confirm).click()
            self.dialog_should_not_be_visible()
            self.wait_until_progress_bar_loaded()
        else:
            self.element(f"//div[@data-cell='{position_of_cell}']").click()
            self.element(self.xpath_split_cells).click()
            self.element(f"//div[@data-door={door_number}]//div[@data-cell='1']").click()

    def check_cells_number(self, number_of_cells, is_planogram=False, door_number=None):
        if not is_planogram:
            self.check_last_table_item_by_header("Qnty of Cells", "4")
            self.element(L.get_indexed(L.edit_button, self.get_table_rows_number())).click()
            self.element("//div[@data-cell]").wait_elements_number(number_of_cells)
            self.element(L.label_cancel).click()
            self.dialog_should_not_be_visible()
            self.wait_until_progress_bar_loaded()
        else:
            self.element(f"//div[@data-door={door_number}]//div[@data-cell]").wait_elements_number(number_of_cells)

    def assign_smart_shelf_to_locker(self, smart_shelf, locker, door_number):
        self.open_last_page()
        row_number = self.get_row_of_table_item_by_header(smart_shelf, "Serial Number")
        self.element(L.get_indexed(L.table_row, row_number)+L.edit_button).click()
        self.wait_until_progress_bar_loaded()
        # input Assign To and check if Door Number is editable
        self.select_in_dropdown(L.get_dropdown_in_dialog(1), locker)
        self.element(L.get_dropdown_in_dialog(2)).wait_until_enabled()
        # input Door Number
        self.select_in_dropdown(L.get_dropdown_in_dialog(2), door_number)
        self.element(L.submit_button).click()
        self.dialog_should_not_be_visible()
        self.wait_until_progress_bar_loaded()
