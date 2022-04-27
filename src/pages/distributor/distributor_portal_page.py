from src.pages.base_page import BasePage

class DistributorPortalPage(BasePage):
    def sidebar_account_status(self):
        self.element("//button[@data-testid='status-button']/..").click()

    def sidebar_users(self):
        self.element("//div[@id='sidebar-users-groups']").click()

    def sidebar_warehouses(self):
        self.element("//div[@id='sidebar-warehouses']").click()

    def sidebar_customers(self):
        self.element("//div[@id='sidebar-customers']").click()

    def sidebar_catalog(self):
        self.element("//div[@id='sidebar-catalog']").click()

    def sidebar_pricing(self):
        self.element("//div[@id='sidebar-pricing']").click()

    def sidebar_settings(self):
        self.element("//div[@id='sidebar-settings']").click()

    def sign_out(self):
        self.element("//div[@id='sidebar-sign_out']").click()

    def sidebar_rfid(self):
        self.element("//div[@id='sidebar-rfid']").click()

    def sidebar_serialization(self):
        self.element("//div[@id='sidebar-lot-serialization']").click()

    def sidebar_hardware(self):
        self.element("//div[@id='sidebar-hardware']").click()

    def sidebar_order_status(self):
        self.element("//div[@id='sidebar-order-status']").click()

    def sidebar_support(self):
        self.element("//div[@id='sidebar-support']").click()

    def distributor_sidebar_should_contain_email(self, email=None):
        if email is None:
            email = self.context.distributor_email
        self.element(f"//span[text()='{email}']").get()
