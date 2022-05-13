from src.pages.customer.customer_portal_page import CustomerPortalPage
from src.pages.locator import Locator as L
from glbl import Log, Error

class ReorderListPage(CustomerPortalPage):
    xpath_po_dialog_row = "//table/tbody/tr"
    xpath_po_dialog_column = "//td"
    xpath_replenishment_item = "//div[@data-testid='replenishment-item']"
    xpath_replenishment_item_sku = "//div[@data-testid='part-sku']"
    xpath_submit_reorder_list_button = "//button/span[text()='Submit']"

    def unselect_all(self):
        self.unselect_checkbox(L.get_indexed(L.checkbox, 1))

    def select_by_sku(self, expected_sku):
        replenishment_items_count = self.element(self.xpath_replenishment_item).count()
        for index in range(1, replenishment_items_count+1):
            item_xpath = L.get_indexed(self.xpath_replenishment_item, index)
            sku_xpath = item_xpath+self.xpath_replenishment_item_sku
            actual_sku = self.element(sku_xpath).text()
            if actual_sku == expected_sku:
                self.select_checkbox(item_xpath+L.checkbox)
                break
        else:
            Error.error(f"Replenishment item with SKU = '{expected_sku}' not found")

    def get_item_xpath_in_po_dialog(self, row, column):
        return f"(({L.dialog}{self.xpath_po_dialog_row})[{row}]{self.xpath_po_dialog_column})[{column}]"

    def get_item_text_in_po_dialog(self, row, column):
        item_xpath = self.get_item_xpath_in_po_dialog(row, column)
        return self.element(item_xpath).text()

    def check_po_number_in_dialog(self, po_number_body):
        self.element(self.xpath_submit_reorder_list_button).click()
        rows_count = self.element(self.xpath_po_dialog_row).count()
        for shipto in po_number_body.keys():
            self.element(f"{L.dialog}//td[text()='{shipto}']").get()
            for index in range(1, rows_count+1):
                if self.get_item_text_in_po_dialog(index, 1) == shipto:
                    po_value = self.element(f"{self.get_item_xpath_in_po_dialog(index, 4)}//input[@type='text']").get().get_attribute("value")
                    if po_number_body[shipto] == po_value:
                        Log.info(f"PO number of '{shipto}' shipto is correct")
                    else:
                        Error.error(f"PO number of '{shipto}' shipto is incorrect")
                    break
            else:
                Error.error(f"There is no shipto '{shipto}' in dialog")
        self.element(L.cancel_button).click()
        self.dialog_should_not_be_visible()

    def submit_replenishment_list_different_po(self, po_number_body):
        self.element(self.xpath_submit_reorder_list_button).click()
        self.set_slider(L.dialog+L.checkbox, "false")
        for shipto in po_number_body.keys():
            self.element(f"{L.dialog}//td[text()='{shipto}']").get()
            rows_count = self.element(self.xpath_po_dialog_row).count()
            for index in range(1, rows_count+1):
                if self.get_item_text_in_po_dialog(index, 1) == shipto:
                    self.element(self.get_item_xpath_in_po_dialog(index, 4)+L.type_text).enter(po_number_body[shipto])
                    break
            else:
                Error.error(f"There is no shipto '{shipto}' in dialog")
        self.element(L.submit_button).click()
        self.element(L.successfully_submitted_reorder_list).get()

    def submit_replenishment_list_general_po(self, po_number):
        self.element(self.xpath_submit_reorder_list_button).click()
        self.set_slider(L.dialog+L.checkbox, "true")
        self.element(L.get_indexed(L.dialog+L.type_text, 1)).enter(po_number)
        self.element(L.submit_button).click()
        self.element(L.successfully_submitted_reorder_list).get()
