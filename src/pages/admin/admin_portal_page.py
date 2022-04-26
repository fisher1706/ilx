from src.pages.base_page import BasePage

class AdminPortalPage(BasePage):
    def sign_out(self):
        self.element("//div[@id='sidebar-sign-out']").click()

    def sidebar_hardware(self):
        self.element("//div[@id='sidebar-hardware']").click()

    def sidebar_universal_catalog(self):
        self.element("//div[@id='sidebar-universal-catalog']").click()

    def sidebar_distributors(self):
        self.element("//div[@id='sidebar-distributors']").click()

    def sidebar_fees(self):
        self.element("//div[@id='sidebar-fees']").click()
