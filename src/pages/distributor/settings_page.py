import os
from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class SettingsPage(DistributorPortalPage):
    def import_document(self):
        self.wait_until_page_loaded()
        start_number_of_rows = self.get_element_count(L.xpath_by_count(L.xpath_table, 1) + L.xpath_table_row)
        Tools.generate_csv("doc.pdf", [[1, 2]])
        folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        folder += "/output/doc.pdf"
        self.get_element_by_id(L.id_file_upload).send_keys(folder)
        self.get_element_by_xpath(L.xpath_successfully_uploaded_document_msg)
        self.elements_count_should_be(L.xpath_by_count(L.xpath_table, 1) + L.xpath_table_row, start_number_of_rows+1)

    def delete_last_document(self):
        start_number_of_rows = self.get_element_count(L.xpath_by_count(L.xpath_table, 1) + L.xpath_table_row)
        self.click_xpath(L.xpath_by_count(L.xpath_remove_button, start_number_of_rows))
        self.click_xpath(L.xpath_dialog + L.xpath_submit_button)
        self.dialog_should_not_be_visible()
        self.elements_count_should_be(L.xpath_by_count(L.xpath_table, 1) + L.xpath_table_row, start_number_of_rows-1)
