class IlxSessionContext:
    ilx_testrail_email = None
    ilx_testrail_password = None
    ilx_environment = None
    ilx_base_data = None
    ilx_credentials = None

    ilx_erp_token = None

    edi_856_auth_token = None
    user_name_edi_856 = None
    password_edi_856 = None

    ilx_infor_token = None

    ilx_browser_name = None
    ilx_driver = None
    ilx_url = None
    ilx_email = None
    ilx_password = None

    ilx_qa_token = None

    srx_url = None

    srx_email_dist = None
    srx_password_dist = None

    srx_email_customer = None
    srx_password_customer = None

    srx_auth = None

    srx_settings_email_search_product = None

    def __setattr__(self, key, value):
        if hasattr(self, key):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Cannot create new attribute for class Context")


class IlxContext:
    ilx_testrail_run_id = None
    ilx_testrail_case_id = None
    ilx_testrail_status_id = None
    ilx_testrail_comment = None
    ilx_session_context = None
    ilx_data = None

    ilx_erp_token = None

    edi_856_auth_token = None
    user_name_edi_856 = None
    password_edi_856 = None

    ilx_infor_token = None

    ilx_browser_name = None
    ilx_driver = None
    ilx_url = None
    ilx_email = None
    ilx_password = None

    ilx_qa_token = None

    srx_url = None

    srx_email_dist = None
    srx_password_dist = None

    srx_email_customer = None
    srx_password_customer = None

    srx_auth = None

    srx_settings_email_search_product = None

    def __setattr__(self, key, value):
        if hasattr(self, key):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Cannot create new attribute for class Context")
