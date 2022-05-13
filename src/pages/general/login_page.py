from src.pages.base_page import BasePage
from src.pages.locator import Locator as L

class LoginPage(BasePage):
    #----FOLLOW URL----
    def follow_admin_portal(self):
        self.follow_url(self.url.admin_portal)

    def follow_auth_portal(self):
        self.follow_url(self.url.auth_portal)

    def follow_checkout_portal(self):
        self.follow_url(self.url.checkout_portal)

    def follow_new_checkout_portal(self):
        self.follow_url(self.url.new_checkout_portal)

    #----FIELDS AND BUTTONS----
    def input_email(self, email):
        self.element(L.email).enter(email)

    def input_password(self, password):
        self.element(L.password).enter(password, hide_log=True)

    def clear_email(self):
        self.element(L.email).enter("")

    def clear_password(self):
        self.element(L.password).enter("")

    def click_on_submit_button(self):
        self.element(L.submit_button).click()

    def click_on_submit_button_checkout(self):
        self.element("//ion-button[@type='submit']").click()

    def open_forgot_password_page(self):
        self.element(L.forgot_password).click()

    def return_from_forgot_password_page(self):
        self.element("//a[@href='/sign-in']").click()

    #----CHECKS----
    def error_should_be_present(self):
        self.element("//span[text()='Incorrect email address or password.']").get()

    def invalid_email_message_should_be_present(self):
        self.element("//p[text()='Email must be a valid email']").get()

    def required_email_message_should_be_present(self):
        self.element("//p[text()='Email is a required field']").get()

    def required_password_message_should_be_present(self):
        self.element("//p[text()='Please enter password']").get()

    def it_should_be_login_page(self):
        self.element(L.forgot_password).get()
        self.element(L.email).get()
        self.element(L.password).get()

    def incorrect_email_message_should_be_present(self):
        self.element("//span[text()='Please check if the entered email address is correct and try again.']").get()

    def submit_button_should_be_disabled(self):
        self.element(L.submit_button).wait_until_disabled()

    def submit_button_should_be_enabled(self):
        self.element(L.submit_button).wait_until_enabled()

    #----FULL LOG IN----
    def log_in_admin_portal(self):
        self.follow_admin_portal()
        self.input_email(self.context.admin_email)
        self.input_password(self.context.admin_password)
        self.click_on_submit_button()

    def log_in_distributor_portal(self, email=None, password=None, expected_url=None):
        self.follow_auth_portal()
        if email is None:
            email = self.context.distributor_email
        if password is None:
            password = self.context.distributor_password
        self.input_email(email)
        self.input_password(password)
        self.click_on_submit_button()
        self.title_should_be("SRX Distributor Portal")
        self.follow_url(self.url.distributor_portal, expected_url=expected_url)

    def log_in_customer_portal(self, email=None, password=None):
        self.follow_auth_portal()
        if email is None:
            email = self.context.customer_email
        if password is None:
            password = self.context.customer_password
        self.input_email(email)
        self.input_password(password)
        self.click_on_submit_button()
        self.title_should_be("SRX User Dashboard")
        self.follow_url(self.url.customer_portal)
        self.element(L.role_button).click()
