from src.pages.base_page import BasePage
from src.pages.locator import Locator as L

class NewCheckoutPortalPage(BasePage):
    def input_passcode(self, passcode):
        self.input_by_name("passcode", passcode)

    def log_out_checkout_portal(self):
        self.element("//ion-item[@class='menu-item item md item-lines-none item-fill-none in-list ion-activatable ion-focusable hydrated']").click()

    def log_out_checkout_group(self):
        self.element("//*[@class='sc-ion-buttons-md-h sc-ion-buttons-md-s md hydrated']")
        self.element("//*[@id='ion-overlay-1']/div[2]/div[2]/srx-checkout-group-popover/ion-list/ion-item")
        self.element("//*[@class ='alert-button ion-focusable ion-activatable alert-button-role-ok sc-ion-alert-md']")

    def select_issue(self):
        self.element("//*[@class='md ion-activatable hydrated'][1]").click()

    def select_return(self):
        self.element("//*[@class='md ion-activatable hydrated'][2]").click()

    def open_hide_menu(self):
        self.element("//ion-menu-button[@class='md button in-toolbar in-toolbar-color ion-activatable ion-focusable hydrated']").click()

    def wrong_user_error_should_be_present(self):
        assert self.element("//div[@class='error-container']").text() == "PreAuthentication failed with error User does not exist.."

    def wrong_password_error_should_be_present(self):
        assert self.element("//div[@class='error-container']").text() == "Incorrect username or password."

    def wrong_passcode_error_should_be_present(self):
        assert self.element("//div[@class='error-container']").text() == "User doesnˈt have permissions to complete this action."

    def signin_button_should_be_disabled(self):
        self.element("//div[@class='submit-container']").wait_until_disabled()
