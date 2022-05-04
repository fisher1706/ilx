from src.pages.base_page import BasePage

class CustomerPortalPage(BasePage):
    def sidebar_users_and_groups(self):
        self.element("//div[@id='sidebar-users_and_groups']").click()

    def sidebar_allocation_codes(self):
        self.element("//div[@id='sidebar-allocation_codes']").click()

    def sidebar_activity_feed(self):
        self.element("//div[@id='sidebar-activity_feed']").click()

    def sidebar_orders_and_quotes(self):
        self.element("//div[@id='sidebar-quoted_ordered_list']").click()

    def sign_out(self):
        self.element("//div[@id='sidebar-sign_out']").click()

    def sidebar_assets(self):
        self.element("//div[@id='sidebar-assets']").click()

    def customer_sidebar_should_contain_email(self, email=None):
        if email is None:
            email = self.context.customer_email
        self.element(f"//span[text()='{email}']").get()
