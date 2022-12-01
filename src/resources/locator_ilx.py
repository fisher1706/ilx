class LocatorIlx:

    # NAMEs
    ilx_email = 'email'
    ilx_password = 'password'
    group_name = 'name'
    group_path = 'path'
    data = 'group-item'
    confirm = 'confirm'
    int_base_path = 'basePath'
    int_group_path = 'groupPath'

    # XPATHs
    user_email = '//*[@id="root"]/div[2]/div/div/div[2]/ul/div[1]/div[2]'
    group_create = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'
    group_delete = '//*[@id="context-actions-menu"]/div[3]/ul/li[2]/span[1]'
    button_group_del = '/html/body/div[2]/div[3]/div/div[3]/button[2]/span'
    before_button_remove_from_group = '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div/div/div/div[1]/div[3]/button'
    button_remove_from_group = '//*[@id="context-actions-menu"]/div[3]/ul/li[2]/span[1]'
    remove_from_group = '/html/body/div[2]/div[3]/div/div[2]/div[4]/div/div/input'
    after_button_remove_from_group = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
    access = '//*[@id="sidebar-item-access"]/div[2]'
    access_before = '//*[@id="sidebar-item-0"]/span'
    button_access_key = '//*[@id="root"]/div[3]/div/div[1]/button'
    input_access_key = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div/div/div/input'
    create_access_key = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'
    group_edit = '//*[@id="context-actions-menu"]/div[3]/ul/li[1]/span[1]'
    input_group_edit = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/input'
    input_path_edit = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/input'
    save_edit_group = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'
    button_create_int = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'
    button_int = '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div'
    button_edit_int = '//*[@id="root"]/div[3]/div/div[2]/button'
    int_name = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div/div/div/input'
    button_int_save = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'
    name_int = '//*[@id="root"]/div[3]/div/div[1]/nav/ol/li[3]/span'
    edit_int = '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div[3]/button/span[1]'
    add_to_group = '//*[@id="context-actions-menu"]/div[3]/ul/li[1]'
    button_add_int = '/html/body/div[2]/div[3]/div/div[2]/div[2]/button[2]'
    edit_group_first = '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/button'
    edit_group_second = '//*[@id="root"]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div[3]/button'
    move_to_group = '//*[@id="context-actions-menu"]/div[3]/ul/li[1]'
    move_int = '/html/body/div[2]/div[3]/div/div[2]/div[2]/button[2]'
    del_int_from_group = '//*[@id="context-actions-menu"]/div[3]/ul/li[3]'
    confirm_delete_from_group = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/input'
    delete_int_from_group = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
    remove_int_from_group = '//*[@id="context-actions-menu"]/div[3]/ul/li[2]'
    confirm_remove_int = '/html/body/div[2]/div[3]/div/div[2]/div[4]/div/div/input'
    button_remove_int = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
    delete_int_first = '//*[@id="context-actions-menu"]/div[3]/ul/li[2]'
    confirm_delete_int = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/input'
    delete_int_second = '/html/body/div[2]/div[3]/div/div[3]/button[2]'

    connection = '//*[@id="sidebar-item-1"]'
    new_connection = '//*[@id="root"]/div[3]/div/div[1]/button'
    connection_name = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/input'
    connection_url = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[2]/div/div/input'
    connection_save = '/html/body/div[2]/div[3]/div/div[2]/form/div[2]/button[2]'

    connect_type = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[3]/div/div/div/div/button'
    select_connect = '/html/body/div/div[3]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div/span'
    get_connect = '/html/body/div/div[3]/div/div[1]/nav/ol/li[1]/a'

    int_template = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/div/button'
    int_description = '/html/body/div/div[3]/div/div[3]/div[1]/div/div[2]/div/div/table/tbody/tr/td[1]/div'
    int_auth = '/html/body/div/div[3]/div/div[3]/div[1]/div/div/button[2]/span[1]'
    open_chose_key = '/html/body/div/div[3]/div/div[3]/div[3]/div/form/div[1]/div/div/div/div/div/button'
    save_api_key = '/html/body/div/div[3]/div/div[3]/div[3]/div/form/div[2]/button[2]'
    return_to_int = '/html/body/div/div[3]/div/div[1]/nav/ol/li[3]/a'
    chose_connect_type = "//ul[@role='listbox']/li[@role='option']"
    client_id = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[12]/div/div/input'
    user_name = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[14]/div/div/input'
    client_secret = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[13]/div/div/input'
    connect_passwd = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[15]/div/div/input'
    token_url = '/html/body/div[2]/div[3]/div/div[2]/form/div[1]/div[16]/div/div/input'
    connect_name = '//*[@id="root"]/div[3]/div/div[1]/nav/ol/li[3]'
    connect_chose = '//*[@id="root"]/div[3]/div/div[2]/div[1]/div/div/div[1]/div[3]/button'
    connect_delete = '//*[@id="context-actions-menu"]/div[3]/ul/li[2]'
    chose_connect = '//*[@id="root"]/div[3]/div/div[2]/div/div/div/div[1]/div[1]/span'
    chose_int = '//*[@id="root"]/div[3]/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div/span'
    chose_dest_endpoint = '//*[@id="root"]/div[3]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tbody/tr/td[2]/div'
    confirm_delete_connect = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/input'
    connect_save = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
    data_connects = '//*[@id="sidebar-item-access"]'
    edit_connect = '/html/body/div[2]/div[3]/ul/li[1]'
    connect_name_text = '/html/body/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/span'
    access_key_name = '/html/body/div/div[3]/div/div[3]/div/form/div[1]/div[1]/div/div/input'

    # CLASS_NAMEs
    button = 'MuiButton-label'
    chose_group = 'add-to-group-list-container'
    chose_move_group = 'add-to-group-list-container'
    chose_endpoint = '/html/body/div/div[2]/div/div/div[2]/ul/div[2]/span'

    # TAG_NAMEs
    tag_name = 'li'


class LocatorSrx:
    """customer"""
    chose_type_submit = '//*[@id="root"]/main/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/' \
                        'div[1]/div[2]/div[1]/div[3]/div[3]/div'
    submit_quote = '//*[@id="menu-"]/div[3]/ul/li[1]'
    submit_order = '//*[@id="menu-"]/div[3]/ul/li[2]'

    # IDs
    log_email = 'email'
    log_password = 'password'

    # CLASS_NAMEs
    button = 'MuiButton-label'

    # XPATHs
    chose_order_status = '//*[@id="sidebar-order-status"]/span'
    chose_order = '//*[@id="root"]/main/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div/span/span'
    chose_operation = '//*[@id="item-action-undefined"]/span[1]'
    operation_active = '//*[@id="bulk-operations-menu"]/div[3]/ul/div[2]/div/div/ul/div[1]/div/span'
    path_onboard = '//*[@id="sidebar-onboarding"]/span'
    path_sign_out = '//*[@id="sidebar-sign_out"]/span'

    chose_customer = '//*[@id="sidebar-customers"]/span'
    chose_customer_name = '//*[@id="root"]/main/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span'
    chose_ship_to = '//*[@id="root"]/main/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div/span'
    list_right_wmi_data = '//*[@id="root"]/header/div/div/div/div[4]'
    vmi_list_settings = '//*[@id="root"]/header/div/div/div/div[3]/div/button[9]/span[1]'
    reorder_list_submit_integration = '//*[@id="root"]/main/div/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/span'
    use_default = '//*[@id="root"]/main/div/div[2]/div[4]/div/div[1]/div[1]/div/div[3]/div/' \
                  'fieldset/label/span[1]/span[1]/span[1]/input'
    check_use_default = '//*[@id="root"]/main/div/div[2]/div[4]/div/div[1]/div[1]/div/div[3]/div/' \
                        'fieldset/label/span[1]/span[1]/span[1]'
    integration_logix_api = '//*[@id="rlSubmitIntegrationSettings-shiptosettings-settings-form"]' \
                            '/div/div/div[1]/div/fieldset/div[2]/label[3]/span[1]/span[1]'
    save_vmi_list_settings = '//*[@id="root"]/main/div/div[2]/div[4]/div/div[2]/div/div/div/div[2]/button[2]/span[1]'

    chose_order_status_before = '//*[@id="bulk-operations-menu"]/div[3]/ul/div[2]/div/div/ul/div[2]/div/span'
    off_filter = '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div/div[1]/div/button/span[1]'
    on_filter = '//*[@id="root"]/main/div/div[2]/div/div[1]/div[1]/div/div[2]/button/span[1]/span'
    chose_external_id = '//*[@id="Transaction-filters-popup"]/div[3]/ul/li[6]'
    set_external_id = '//*[@id="Transaction-filter-input-erpOrderId"]'

    order_status = '//*[@id="root"]/main/div/div[3]/div/div[1]/div[2]'
    order_status_api = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                       '/div/div[1]/div[1]/fieldset/div[2]/label[1]/span[1]/span[1]/input'
    check_order_status_api = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                             '/div/div[1]/div[1]/fieldset/div[2]/label[1]/span[1]'
    order_status_srx_ui = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                          '/div/div[1]/div[1]/fieldset/div[2]/label[2]/span[1]/span[1]/input'
    check_order_status_srx_ui = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                                '/div/div[1]/div[1]/fieldset/div[2]/label[2]/span[1]/span[1]'
    order_status_il_api = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]/div/div[1]' \
                          '/div[1]/fieldset/div[2]/label[3]/span[1]/span[1]/input'
    check_order_status_il_api = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                                '/div/div[1]/div[1]/fieldset/div[2]/label[3]/span[1]/span[1]'
    save_settings_order_status = '//*[@id="orderStatus-erpintegrationsettings-settings-form"]' \
                                 '/div/div[2]/div/button[2]/span[1]'
    auto_submit_schedule = '//*[@id="root"]/main/div/div[2]/div[1]/div/div[1]/div[2]/span[1]'
    use_default_auto_submit_schedule = '//*[@id="root"]/main/div/div[2]/div[1]/div/div[1]/div[1]' \
                                       '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]/input'
    check_use_default_auto_submit_schedule = '//*[@id="root"]/main/div/div[2]/div[1]/div/div[1]/div[1]' \
                                             '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]'
    auto_submit_all_locations = '//*[@id="autoSubmitScheduleSettings-autosubmitschedulesettings-settings-form"]' \
                                '/div/div/div[1]/div/fieldset/div[2]/label[1]/span[1]/span[1]'
    save_settings_auto_submit_schedule = '//*[@id="root"]/main/div/div[2]/div[1]/div/div[2]' \
                                         '/div/div/div/div[2]/button[2]/span[1]'
    reorder_controls = '//*[@id="root"]/main/div/div[2]/div[7]/div/div[1]/div[2]/span[1]'
    use_default_reorder_controls = '//*[@id="root"]/main/div/div[2]/div[7]/div/div[1]/div[1]' \
                                   '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]/input'
    check_use_default_reorder_controls = '//*[@id="root"]/main/div/div[2]/div[7]/div/div[1]/div[1]' \
                                         '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]'
    add_as_issued = '//*[@id="checkoutSoftwareSettings-shiptosettings-settings-form"]' \
                    '/div/div/div[1]/div/fieldset/div[2]/label[2]/span[1]/span[1]'
    save_settings_reorder_controls = '//*[@id="root"]/main/div/div[2]/div[7]/div/div[2]' \
                                     '/div/div/div/div[2]/button[2]/span[1]'

    chose_filter = '//*[@id="root"]/main/div/div[1]/div/div[1]/div[2]/button/span[1]/span'
    by_name = '//*[@id="Customer-filters-popup"]/div[3]/ul/li[1]'
    input_customer_name = '//*[@id="Customer-filter-input-name"]'
    by_ship_to_number = '//*[@id="Shipto-filters-popup"]/div[3]/ul/li[1]'
    input_ship_to_number = '//*[@id="Shipto-filter-input-number"]'
    by_distributor_sku = '//*[@id="VMI-filters-popup"]/div[3]/ul/li[11]'
    input_distributor_sku = '//*[@id="VMI-filter-input-orderingConfig.product.likePartSku"]'
    get_data_from_vmi = '//*[@id="root"]/main/div/div[2]/div/div[1]/div[3]/div/div'
    pricing_information_sources = '//*[@id="root"]/main/div/div[2]/div[13]/div/div[1]/div[2]/span[1]'
    use_default_pricing_information_sources = '//*[@id="root"]/main/div/div[2]/div[13]/div/div[1]/div[1]' \
                                              '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]/input'
    check_use_default_pricing_information_sources = '//*[@id="root"]/main/div/div[2]/div[13]/div/div[1]/div[1]' \
                                                    '/div/div[3]/div/fieldset/label/span[1]/span[1]/span[1]'
    ilx_api = '//*[@id="pricingSource-shiptosettings-settings-form"]' \
              '/div/div/div[1]/div/fieldset/div[2]/label[3]/span[1]/span[1]'
    use_24h_cache_for_price = '//*[@id="pricingSource-shiptosettings-settings-form"]' \
                              '/div/div/div[2]/div/fieldset/label/span[1]/span[1]'
    save_settings_pricing_information_sources = '//*[@id="root"]/main/div/div[2]/div[13]/div/div[2]' \
                                                '/div/div/div/div[2]/button[2]/span[1]'
    vmi_list = '//*[@id="root"]/header/div/div/div/div[3]/div/button[2]/span[1]'

    catalog_data_integration = '//*[@id="root"]/main/div/div[6]/div/div[1]/div[1]/span'
    catalog_data_integration_erp_api = '//*[@id="catalogDataIntegration-erpintegrationsettings-settings-form"]' \
                                       '/div/div[1]/div[2]/div/fieldset/label/span[1]/span[1]/input'
    check_catalog_data_integration_erp_api = '//*[@id="catalogDataIntegration-erpintegrationsettings-settings-form"]' \
                                             '/div/div[1]/div[2]/div/fieldset/label/span[1]/span[1]'
    save_settings_catalog_data_integration = '//*[@id="catalogDataIntegration-erpintegrationsettings-' \
                                                     'settings-form"]/div/div[2]/div/button[2]/span[1]'
    add_location = '//*[@id="item-action-add"]/span'
    enter_to_search = "react-select-2-input"
    chose_catalog = '//*[@id="sidebar-catalog"]/span'
    by_dict_sku_catalog = '//*[@id="Product-filters-popup"]/div[3]/ul/li[1]'
    enter_dist_sku_catalog = '//*[@id="Product-filter-input-partSku"]'
    dist_sku_catalog = '//*[@id="root"]/main/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div[1]/span'

    chose_orders_quotes = '//*[@id="sidebar-quoted_ordered_list"]/span'
    submit_orders_quotes = '//*[@id="root"]/main/div/div[2]/div[3]/button/span[1]'
    set_po_number = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/input'
    submit_number = '/html/body/div[2]/div[3]/div/div[3]/button[2]/span[1]'
    data_order = '//*[@id="root"]/main/div/div[2]/div/div[2]/div/div[1]/div[3]/div/div'

    conf_log_dist = '//*[@id="redirectButton"]'
    path_email = '//*[@id="root"]/div[2]/div/div/div[2]/div/span[2]'

    srx_settings = '//*[@id="sidebar-settings"]/span'
    erp_integration = '//*[@id="root"]/header/div/div/div/div[2]/div/button[2]/span[1]'
    erp_connection = '//*[@id="root"]/main/div/div[1]/div/div[1]/div[1]'
    select_erp = '//*[@id="erpconnectionsettings-general-form"]/div/div[1]/div[1]/div/div/div/div[2]/div'
    integration_logix = '//*[@id="react-select-5-option-3"]'
    site_url = '//*[@id="erpconnectionsettings-general-form"]/div/div[1]/div[7]/div/div/input'
    authorization = '//*[@id="erpconnectionsettings-general-form"]/div/div[1]/div[22]/div/div/input'
    test_connection = '//*[@id="erpconnectionsettings-general-form"]/div/div[1]/div[4]/button/span[1]'
    connect_status = '//*[@id="erpconnectionsettings-general-form"]/div/div[1]/div[2]'
    save_connection = '//*[@id="erpconnectionsettings-general-form"]/div/div[2]/button[3]/span[1]'
    vmi_list_integration = '//*[@id="root"]/main/div/div[7]/div/div[1]/div[1]/span'
    sync_now = '//*[@id="vmiListIntegration-erpintegrationsettings-settings-form"]/div/div[1]/div[6]/button'
    synchronization = '//*[@id="vmiListIntegration-erpintegrationsettings-settings-form"]/div/div[1]/div[6]/div'
    use_erp_api = '//*[@id="vmiListIntegration-erpintegrationsettings-settings-form"]' \
                  '/div/div[1]/div[2]/div/fieldset/label/span[1]/span[1]'
    save_sync = '//*[@id="vmiListIntegration-erpintegrationsettings-settings-form"]/div/div[2]/div/button[2]/span[1]'




