import time

import requests
from selenium.webdriver import Keys

from src.pages.main_page import MainBase
from src.resources.locator_ilx import LocatorSrx
from src.utilities.ilx_utils import Utils


class SrxPage(MainBase):
    def login_srx(self, email, password, path_email):
        self.open_browser(self.srx_url)

        self.is_visible('id', LocatorSrx.log_email).send_keys(email)
        self.is_visible('id', LocatorSrx.log_password).send_keys(password)
        self.is_visible('class_name', LocatorSrx.button).click()
        time.sleep(5)
        self.is_visible('xpath', LocatorSrx.conf_log_dist).click()

        element = self.is_visible('xpath', path_email)
        assert str(element.text) == email, 'Can not login to SRX!'

    def sign_out(self, path_onboard, path_sign_out):
        self.is_visible('xpath', path_onboard).click()
        self.is_visible('xpath', path_sign_out).click()


class SrxPageDistributor(SrxPage):
    def set_settings_erp(self, url='http://3.94.89.202:81/external-api/test-full2/test-full2/',
                         auth='test', msg='Connected'):
        """chose settings"""
        self.is_visible('xpath', LocatorSrx.srx_settings).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.erp_integration).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.erp_connection).click()
        time.sleep(1)

        self.is_visible('xpath', LocatorSrx.select_erp).click()
        self.is_visible('xpath', LocatorSrx.integration_logix).click()

        """set settings"""
        self.is_visible('xpath', LocatorSrx.site_url).send_keys(Keys.CONTROL + "a")
        self.is_visible('xpath', LocatorSrx.site_url).send_keys(Keys.DELETE)
        self.is_visible('xpath', LocatorSrx.site_url).send_keys(url)
        self.is_visible('xpath', LocatorSrx.authorization).send_keys(auth)
        self.is_visible('xpath', LocatorSrx.test_connection).click()
        time.sleep(2)

        """check settings"""
        connect = self.is_visible('xpath', LocatorSrx.connect_status)
        assert connect.text == msg, 'Incorrect status connection! Check mock!'

        self.is_visible('xpath', LocatorSrx.save_connection).click()

        self.refresh_browser()
        self.is_visible('xpath', LocatorSrx.erp_connection).click()
        time.sleep(1)

        site_url = self.is_visible('xpath', LocatorSrx.site_url)
        assert site_url.get_attribute('value') == url, 'Connection is not save!'

    def set_add_settings_erp(self, type_settings):
        self.refresh_browser()

        if type_settings == 'catalog_data_integration':
            self.is_visible('xpath', LocatorSrx.catalog_data_integration).click()

            """set catalog_data_integration_erp_api"""
            erp_api = self.is_present('xpath', LocatorSrx.catalog_data_integration_erp_api).is_selected()
            if not erp_api:
                self.is_visible('xpath', LocatorSrx.check_catalog_data_integration_erp_api).click()
            erp_api = self.is_present('xpath', LocatorSrx.catalog_data_integration_erp_api).is_selected()
            assert erp_api, 'chose erp_api!'

            self.is_visible('xpath', LocatorSrx.save_settings_catalog_data_integration).click()

        elif type_settings == 'order_status':
            self.is_visible('xpath', LocatorSrx.order_status).click()

            """set order_status_api"""
            api = self.is_present('xpath', LocatorSrx.order_status_api).is_selected()
            if not api:
                self.is_visible('xpath', LocatorSrx.check_order_status_api).click()
            api = self.is_present('xpath', LocatorSrx.order_status_api).is_selected()
            assert api, 'chose api!'

            """set order_status_srx_ui"""
            srx_ui = self.is_present('xpath', LocatorSrx.order_status_srx_ui).is_selected()
            if not srx_ui:
                self.is_visible('xpath', LocatorSrx.check_order_status_srx_ui).click()
            srx_ui = self.is_present('xpath', LocatorSrx.order_status_srx_ui).is_selected()
            assert srx_ui, 'chose srx_ui!'

            """set order_status_il_api"""
            il_api = self.is_present('xpath', LocatorSrx.order_status_il_api).is_selected()
            if not il_api:
                self.is_visible('xpath', LocatorSrx.check_order_status_il_api).click()
            il_api = self.is_present('xpath', LocatorSrx.order_status_il_api).is_selected()
            assert il_api, 'chose il_api!'

            self.is_visible('xpath', LocatorSrx.save_settings_order_status).click()

    def set_settings_vmi_list(self, type_settings):
        """chose vmi list settings"""
        self.is_visible('xpath', LocatorSrx.chose_customer).click()
        self.is_visible('xpath', LocatorSrx.chose_customer_name).click()
        self.is_visible('xpath', LocatorSrx.chose_ship_to).click()
        self.is_visible('xpath', LocatorSrx.list_right_wmi_data).click()
        self.is_visible('xpath', LocatorSrx.vmi_list_settings).click()
        time.sleep(3)

        """set vmi list settings"""
        if type_settings == 'reorder_list_submit_integration':
            self.is_visible('xpath', LocatorSrx.reorder_list_submit_integration).click()
            use_default = self.is_present('xpath', LocatorSrx.use_default).is_selected()

            if not use_default:
                self.is_visible('xpath', LocatorSrx.check_use_default).click()
                self.is_visible('xpath', LocatorSrx.check_use_default).click()
            else:
                self.is_visible('xpath', LocatorSrx.check_use_default).click()

            self.is_visible('xpath', LocatorSrx.integration_logix_api).click()
            self.is_visible('xpath', LocatorSrx.save_vmi_list_settings).click()

        elif type_settings == 'auto_submit_schedule':
            self.is_visible('xpath', LocatorSrx.auto_submit_schedule).click()
            use_default = self.is_present('xpath', LocatorSrx.use_default_auto_submit_schedule).is_selected()

            if not use_default:
                self.is_visible('xpath', LocatorSrx.check_use_default_auto_submit_schedule).click()
                self.is_visible('xpath', LocatorSrx.check_use_default_auto_submit_schedule).click()
            else:
                self.is_visible('xpath', LocatorSrx.check_use_default_auto_submit_schedule).click()

            self.is_visible('xpath', LocatorSrx.auto_submit_all_locations).click()
            time.sleep(2)
            self.is_visible('xpath', LocatorSrx.save_settings_auto_submit_schedule).click()

        elif type_settings == 'reorder_controls':
            self.is_visible('xpath', LocatorSrx.reorder_controls).click()
            use_default = self.is_present('xpath', LocatorSrx.use_default_reorder_controls).is_selected()

            if not use_default:
                self.is_visible('xpath', LocatorSrx.check_use_default_reorder_controls).click()
                self.is_visible('xpath', LocatorSrx.check_use_default_reorder_controls).click()
            else:
                self.is_visible('xpath', LocatorSrx.check_use_default_reorder_controls).click()

            self.is_visible('xpath', LocatorSrx.add_as_issued).click()
            time.sleep(2)
            self.is_visible('xpath', LocatorSrx.save_settings_reorder_controls).click()

    def sync_vmi(self):
        """chose vmi list integration"""
        self.is_visible('xpath', LocatorSrx.srx_settings).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.erp_integration).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.vmi_list_integration).click()

        """sync now"""
        sync_now = self.is_visible('xpath', LocatorSrx.sync_now)
        if sync_now:
            sync_now.click()
            synchronization = self.is_visible('xpath', LocatorSrx.synchronization)
            return synchronization.text
        else:
            self.is_visible('xpath', LocatorSrx.use_erp_api).click()
            # self.is_visible('xpath', LocatorSrx.save_sync).click()
            self.is_visible('xpath', LocatorSrx.sync_now).click()

            synchronization = self.is_visible('xpath', LocatorSrx.synchronization)
            return synchronization.text

    def activate_order_status(self):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        self.set_settings_erp()
        self.set_settings_vmi_list(type_settings='reorder_list_submit_integration')

        """activate_order"""
        self.is_visible('xpath', LocatorSrx.chose_order_status).click()
        self.is_visible('xpath', LocatorSrx.chose_order).click()
        self.is_visible('xpath', LocatorSrx.chose_operation).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.operation_active).click()

        self.sign_out(LocatorSrx.path_onboard, LocatorSrx.path_sign_out)

    def check_order_status(self, product, submit_type):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        """get data order"""
        self.is_visible('xpath', LocatorSrx.chose_order_status).click()
        data_order = self.is_visible('xpath', LocatorSrx.data_order).text.split('\n')
        print(f'\ndata order: {data_order}')
        assert product == data_order[10], 'Incorrect number of product!'
        if submit_type == 'quote':
            assert data_order[13] == 'QUOTED', 'Incorrect order status!'
        else:
            assert data_order[13] == 'ORDERED', 'Incorrect order status!'

        return data_order[1]

    def get_data_order_status(self, host_name='qa', dist_id=1514, dist_sku=123):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        self.set_settings_erp()
        self.set_add_settings_erp(type_settings='order_status')
        self.set_settings_vmi_list(type_settings='auto_submit_schedule')
        self.set_settings_vmi_list(type_settings='reorder_controls')

        """set data order before test"""
        self.is_visible('xpath', LocatorSrx.chose_order_status).click()
        self.is_visible('xpath', LocatorSrx.chose_order).click()
        self.is_visible('xpath', LocatorSrx.chose_operation).click()
        time.sleep(3)
        self.is_visible('xpath', LocatorSrx.chose_order_status_before).click()
        time.sleep(1)

        data_order = self.is_visible('xpath', LocatorSrx.data_order).text.split('\n')
        print(f'\ndata order: {data_order}')

        external_id = data_order[1]
        dist_sku_srx = data_order[4]
        assert dist_sku_srx == str(dist_sku), 'check dist_sku!'

        """send request"""
        url = f'https://api-{host_name}.storeroomlogix.com/admin-portal/admin/orders/erp-test/' \
              f'get-order-status?orderId={external_id}&isV2Api=true&distributorId={dist_id}'

        headers = {'Authorization': self.srx_auth}

        resp = requests.get(url=url, headers=headers)
        assert resp.status_code == 200, 'check srx_auth or mock!'

        """get data order after test"""
        self.refresh_browser()
        time.sleep(5)
        self.is_visible('xpath', LocatorSrx.chose_order_status).click()

        self.is_visible('xpath', LocatorSrx.off_filter).click()
        time.sleep(1)
        self.is_visible('xpath', LocatorSrx.on_filter).click()
        self.is_visible('xpath', LocatorSrx.chose_external_id).click()
        self.is_visible('xpath', LocatorSrx.set_external_id).send_keys(external_id)
        self.is_visible('xpath', LocatorSrx.set_external_id).send_keys(Keys.ENTER)
        time.sleep(3)

        data_order = self.is_visible('xpath', LocatorSrx.data_order).text.split('\n')
        print(f'\ndata order: {data_order}')

        qnt = data_order[9]
        status = data_order[13]

        return qnt, status

    def get_pricing(self, customer='cust_1', ship_to='1', sku='123'):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        self.set_settings_erp()

        """chose customer"""
        self.is_visible('xpath', LocatorSrx.chose_customer).click()
        self.is_visible('xpath', LocatorSrx.chose_filter).click()
        self.is_visible('xpath', LocatorSrx.by_name).click()
        self.is_visible('xpath', LocatorSrx.input_customer_name).send_keys(customer)
        self.is_visible('xpath', LocatorSrx.input_customer_name).send_keys(Keys.ENTER)

        """chose ship_to"""
        self.is_visible('xpath', LocatorSrx.chose_ship_to).click()
        self.is_visible('xpath', LocatorSrx.chose_filter).click()
        self.is_visible('xpath', LocatorSrx.by_ship_to_number).click()
        self.is_visible('xpath', LocatorSrx.input_ship_to_number).send_keys(ship_to)
        self.is_visible('xpath', LocatorSrx.input_ship_to_number).send_keys(Keys.ENTER)

        """chose sku"""
        self.is_visible('xpath', LocatorSrx.chose_ship_to).click()
        self.is_visible('xpath', LocatorSrx.chose_filter).click()
        self.is_visible('xpath', LocatorSrx.by_distributor_sku).click()
        self.is_visible('xpath', LocatorSrx.input_distributor_sku).send_keys(sku)
        self.is_visible('xpath', LocatorSrx.input_distributor_sku).send_keys(Keys.ENTER)

        """get data before"""
        el_1 = self.is_visible('xpath', LocatorSrx.get_data_from_vmi)
        data_1 = el_1.text.split('\n')
        print(f'\ndata before test: {data_1}')

        """"settings pricing_information_sources"""
        self.is_visible('xpath', LocatorSrx.list_right_wmi_data).click()
        self.is_visible('xpath', LocatorSrx.vmi_list_settings).click()
        self.is_visible('xpath', LocatorSrx.pricing_information_sources).click()

        use_default = self.is_present('xpath', LocatorSrx.use_default_pricing_information_sources).is_selected()
        if not use_default:
            self.is_visible('xpath', LocatorSrx.check_use_default_pricing_information_sources).click()
            self.is_visible('xpath', LocatorSrx.check_use_default_pricing_information_sources).click()
        else:
            self.is_visible('xpath', LocatorSrx.check_use_default_pricing_information_sources).click()

        self.is_visible('xpath', LocatorSrx.ilx_api).click()
        self.is_visible('xpath', LocatorSrx.use_24h_cache_for_price).click()
        self.is_visible('xpath', LocatorSrx.save_settings_pricing_information_sources).click()

        """return for vmi"""
        self.is_visible('xpath', LocatorSrx.vmi_list).click()
        self.refresh_browser()
        time.sleep(3)

        """chose sku"""
        self.is_visible('xpath', LocatorSrx.chose_filter).click()
        self.is_visible('xpath', LocatorSrx.by_distributor_sku).click()
        self.is_visible('xpath', LocatorSrx.input_distributor_sku).send_keys(sku)
        self.is_visible('xpath', LocatorSrx.input_distributor_sku).send_keys(Keys.ENTER)

        """get data after"""
        el_2 = self.is_visible('xpath', LocatorSrx.get_data_from_vmi)
        data_2 = el_2.text.split('\n')
        print(f'\ndata after test: {data_2}')

        return data_1, data_2

    def vmi_list_sync(self):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)
        self.set_settings_erp()

        synch = self.sync_vmi()
        return synch

    def set_settings_search_product(self):
        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        self.set_settings_erp(self.srx_settings_email_search_product, self.qa_token)
        self.set_add_settings_erp(type_settings='catalog_data_integration')

        self.sign_out(LocatorSrx.path_onboard, LocatorSrx.path_sign_out)

    def search_product(self):
        dsku = Utils.random_str()

        self.login_srx(self.srx_email_dist, self.srx_password_dist, LocatorSrx.path_email)

        """chose vmi_list"""
        self.is_visible('xpath', LocatorSrx.chose_customer).click()
        self.is_visible('xpath', LocatorSrx.chose_customer_name).click()
        time.sleep(5)
        self.is_visible('xpath', LocatorSrx.chose_ship_to).click()

        """add location"""
        self.is_visible('xpath', LocatorSrx.add_location).click()
        self.is_visible('id', LocatorSrx.enter_to_search).send_keys(dsku)
        self.is_visible('id', LocatorSrx.enter_to_search).send_keys(Keys.ENTER)
        time.sleep(1)

        """check catalog"""
        self.refresh_browser()
        self.is_visible('xpath', LocatorSrx.chose_catalog).click()
        self.is_visible('xpath', LocatorSrx.chose_filter).click()
        self.is_visible('xpath', LocatorSrx.by_dict_sku_catalog).click()
        self.is_visible('xpath', LocatorSrx.enter_dist_sku_catalog).send_keys(dsku)
        self.is_visible('xpath', LocatorSrx.enter_dist_sku_catalog).send_keys(Keys.ENTER)
        time.sleep(2)
        el = self.is_visible('xpath', LocatorSrx.dist_sku_catalog)
        return el.text


class SrxPageCustomer(SrxPage):
    def submit_orders_quotes(self, submit_type='quote'):
        product = Utils.random_str()
        self.login_srx(self.srx_email_customer, self.srx_password_customer, LocatorSrx.path_email)

        """submit"""
        self.is_visible('xpath', LocatorSrx.chose_orders_quotes).click()
        self.is_visible('xpath', LocatorSrx.chose_type_submit).click()

        if submit_type == 'quote':
            self.is_visible('xpath', LocatorSrx.submit_quote).click()
        else:
            self.is_visible('xpath', LocatorSrx.submit_order).click()

        self.is_visible('xpath', LocatorSrx.submit_orders_quotes).click()
        self.is_visible('xpath', LocatorSrx.set_po_number).send_keys(product)
        self.is_visible('xpath', LocatorSrx.submit_number).click()
        time.sleep(3)

        self.sign_out(LocatorSrx.path_onboard, LocatorSrx.path_sign_out)
        return product, submit_type
