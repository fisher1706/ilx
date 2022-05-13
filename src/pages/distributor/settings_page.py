import os
from src.pages.distributor.distributor_portal_page import DistributorPortalPage
from src.pages.locator import Locator as L
from src.resources.tools import Tools

class SettingsPage(DistributorPortalPage):
    def import_document(self):
        Tools.generate_csv("doc.pdf", [[1, 2]])
        folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        folder += "/output/doc.pdf"
        self.element(L.file_upload).get().send_keys(folder)
        self.element(L.successfully_uploaded_document_msg)

    def delete_last_document(self):
        self.element(L.last_role_row + L.remove_button).click()
        self.element(L.dialog + L.submit_button).click()
        self.dialog_should_not_be_visible()
