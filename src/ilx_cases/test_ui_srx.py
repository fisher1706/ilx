import pytest
from src.pages.ilx.srx_page import SrxPageDistributor, SrxPageCustomer
from src.pages.ilx.ilx_utils_ui import IlxUtils


def test_sales_order_sales_order_quote(ui_ilx):
    ui_ilx.ilx_testrail_case_id = 12857

    SrxPageDistributor(ui_ilx).activate_order_status()
    product, submit_type = SrxPageCustomer(ui_ilx).submit_orders_quotes()
    external_id = SrxPageDistributor(ui_ilx).check_order_status(product, submit_type)
    assert external_id


def test_sales_orders_status(ui_ilx):
    ui_ilx.ilx_testrail_case_id = 12858

    qnt, status = SrxPageDistributor(ui_ilx).get_data_order_status()
    assert qnt == '30', 'incorrect qnt!'
    assert status == 'ORDERED', 'incorrect status!'


def test_get_pricing_integration(ui_ilx):
    ui_ilx.ilx_testrail_case_id = 12859

    before, after = SrxPageDistributor(ui_ilx).get_pricing()
    delta = IlxUtils.diff(before, after)
    print(f'delta: {delta}')
    assert delta, 'check mock settings!'


def test_vmi_list_sync(ui_ilx):
    ui_ilx.ilx_testrail_case_id = 13742

    synch = SrxPageDistributor(ui_ilx).vmi_list_sync()
    assert synch == 'Synchronization started'


def test_search_product(ui_ilx):
    ui_ilx.ilx_testrail_case_id = 13743

    SrxPageDistributor(ui_ilx).set_settings_search_product()
    dsku = SrxPageDistributor(ui_ilx).search_product()
    assert dsku, 'check mock settings!'
