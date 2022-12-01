class IlxData:

    'The class contains the predefined data using in regression tests'

    def __init__(self, environment):
        if environment == 'dev':
            self.dev_environment()
        elif environment == 'qa':
            self.qa_environment()
        elif environment == 'prod':
            self.prod_environment()

    def dev_environment(self):
        pass

    def prod_environment(self):
        pass

    def qa_environment(self):
        # ILX-ERP
        self.ilx_url = 'https://api.qa.integrationlogix.com/external-api/' \
                       'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/submit_order/salesOrdersStatusV2'

        # EDI_856
        self.edi_856_url = 'https://api.qa.integrationlogix.com/external-api/' \
                           'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/salesOrdersStatus/salesOrdersStatus'

        # self.edi_856_url = 'https://api.qa.integrationlogix.com/external-api/' \
        #                    'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/edi_856_bsn/salesOrdersStatus'

        # self.edi_856_url = 'https://api.qa.integrationlogix.com/external-api/' \
        #                    'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/edi_856_ref_re/salesOrdersStatus'

        self.path_out = '/home/oleg/PycharmProjects/srx-robot/src/ilx_cases/outbox/'
        self.path_in = '.src/ilx_cases/inbox/'

        # self.host_edi_856 = 'ftps.qa.integrationlogix.com'
        # self.inbox_edi_856 = '/edi_856_bsn_salesOrdersStatus/EDI/X12_856/Inbox'
        # self.reject_edi_856 = '/edi_856_bsn_salesOrdersStatus/EDI/X12_856/Rejected'
        # self.outbox_edi_856 = '/edi_856_bsn_salesOrdersStatus/EDI/X12_856/Outbox'

        # self.host_edi_856 = 'ftps.qa.integrationlogix.com'
        # self.inbox_edi_856 = '/edi_856_ref_re_salesOrdersStatus/EDI/X12_856/Inbox'
        # self.reject_edi_856 = '/edi_856_ref_re_salesOrdersStatus/EDI/X12_856/Rejected'
        # self.outbox_edi_856 = '/edi_856_ref_re_salesOrdersStatus/EDI/X12_856/Outbox'

        self.host_edi_856 = 'ftps.qa.integrationlogix.com'
        self.inbox_edi_856 = '/salesOrdersStatus_salesOrdersStatus/EDI/X12_856/Inbox'
        # self.reject_edi_856 = '/salesOrdersStatus_salesOrdersStatus/EDI/X12_856/Rejected'
        # self.outbox_edi_856 = '/salesOrdersStatus_salesOrdersStatus/EDI/X12_856/Outbox'

        # self.host_edi_856 = 'ftps.integrationlogix.com'
        # self.inbox_edi_856 = '/salesOrdersStatusV2_salesOrdersStatusV2/EDI/X12_856/Inbox'
        # self.reject_edi_856 = '/salesOrdersStatusV2_salesOrdersStatusV2/EDI/X12_856/Rejected'
        # self.outbox_edi_856 = '/salesOrdersStatusV2_salesOrdersStatusV2/EDI/X12_856/Outbox'

        # INFOR
        self.ilx_infor_url = 'https://api.qa.integrationlogix.com/external-api' \
                             '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/infor_test/infor_test'

        # WMI
        self.ilx_wmi_url = 'https://api.qa.integrationlogix.com/external-api' \
                           '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/vmi_sync/vmi_sync'

        # BILLING
        self.ilx_billing_url = 'https://api.qa.integrationlogix.com/external-api' \
                               '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/submitBilling/submitBilling'

        # ECLIPSE PRICE
        self.eclipse_pricing_url = 'https://api.qa.integrationlogix.com/external-api' \
                                   '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/get_pricing_eclipse/get_pricing_eclipse'

        # JERRIE
        self.ilx_gerrie_url = 'https://api.qa.integrationlogix.com/external-api' \
                              '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/sales_orders_jd/sales_orders_jd'

        # QUOTE INFOR
        self.ilx_quote_infor_url = 'https://api.qa.integrationlogix.com/external-api' \
                                   '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/quote_infor/quote_infor'

        # QUOTE ECLIPSE
        self.ilx_quote_eclipse_url = 'https://api.qa.integrationlogix.com/external-api' \
                                     '/a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/submit_order/quoteOrders'

        # D1 PRICE
        self.ilx_price_d1_url = 'https://api.qa.integrationlogix.com/external-api/' \
                                'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/price_d1/price_d1'

        # INFOR BILLING
        self.ilx_infor_billing_url = 'https://api.qa.integrationlogix.com/external-api/' \
                                     'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/infor_billing/infor_billing'

        # INFOR TRANSFERS
        self.ilx_infor_transfers_url = 'https://api.qa.integrationlogix.com/external-api/' \
                                       'a568e5d3-38d4-4cd1-9aa1-3484afa78a0f/infor_status/infor_status'
