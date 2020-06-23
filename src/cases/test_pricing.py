import pytest
import random
from src.resources.locator import Locator
from src.pages.general.login_page import LoginPage
from src.pages.distributor.pricing_page import PricingPage

class TestPricing():
    @pytest.mark.regression
    def test_pricing_import(self, ui):
        ui.testrail_case_id = 35

        lp = LoginPage(ui)
        pp = PricingPage(ui)
        pricing_body = pp.pricing_body.copy()
        temporary_price = str(random.choice(range(100)))

        #-------------------
        pricing_body["Distributor SKU"] = "PRICING_SKU"
        pricing_body["Price"] = "$"+temporary_price+".00"
        pricing_body["UOM"] = "M"
        pricing_body["Expiration Date"] = "Fri, Dec 12, 2025"
        #-------------------
        pricing = [
            [pricing_body["Distributor SKU"], temporary_price, pricing_body["UOM"], "12/12/2025 10:15:30"]
        ]
        #-------------------

        lp.log_in_distributor_portal()
        pp.sidebar_pricing()
        pp.select_customer_shipto(customer_name=ui.data.customer_name)
        pp.import_pricing(pricing)
        pp.select_customer_shipto(customer_name=ui.data.customer_name)
        pp.check_price_by_name(pricing_body.copy())