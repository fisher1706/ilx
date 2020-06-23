class Data():
    def __init__(self, environment):
        if (environment == 'dev'):
            self.dev_environment()
        elif (environment == 'staging'):
            self.staging_environment()
        elif (environment == 'qa'):
            self.qa_environment()

    def dev_environment(self):
        self.distributor_name = "QA-distributor"
        self.distributor_id = "73"
        self.sub_distributor_name = "Dev Distributor"
        self.testrail_run_id = None
        self.customer_name = "Static Customer"
        self.customer_id = "92"
        self.shipto_number = "2048"
        self.shipto_id = "59"

    def staging_environment(self):
        self.distributor_name = "QA-distributor"
        self.distributor_id = "98"
        self.warehouse_id = "38"
        self.sub_distributor_name = "Static Test"
        self.testrail_run_id = None
        self.customer_name = "Static Customer"
        self.shipto_number = "2048"
        self.testrail_run_id = None
        self.customer_id = "54"
        self.shipto_id = "31"

    def qa_environment(self):
        self.distributor_name = "MAIN-QA-DISTRIBUTOR"
        self.distributor_id = "4"
        self.warehouse_id = "4"
        self.sub_distributor_name = "SECOND-QA-DISTRIBUTOR"
        self.sub_distributor_id = "5"
        self.customer_name = "Static Customer"
        self.shipto_number = "FIRST-QA-SHIPTO"
        self.testrail_run_id = 44
        self.customer_id = "4"
        self.shipto_id = "4"

class SmokeData():
    def __init__(self, environment):
        if (environment == 'dev'):
            self.dev_environment()
        elif (environment == 'staging'):
            self.staging_environment()
        elif (environment == 'qa'):
            self.qa_environment()

    def dev_environment(self):
        pass

    def staging_environment(self):
        self.testrail_run_id = 43
        self.customer_id = "187"
        self.shipto_id = "189"
        self.ordering_config_id = "1516"
        self.testrail_report_id = 6


    def qa_environment(self):
        self.testrail_run_id = 46
        self.customer_id = "191"
        self.shipto_id = "2192"
        self.locker_id = "3869"
        self.ordering_config_id = "2577"
        self.testrail_report_id = 5