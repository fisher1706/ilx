import pytest
import copy
import time
from src.resources.locator import Locator
from src.resources.tools import Tools
from src.pages.distributor.order_status_page import OrderStatusPage
from src.api.setups.setup_location import SetupLocation
from src.api.distributor.shipto_api import ShiptoApi
from src.api.distributor.transaction_api import TransactionApi
from src.api.distributor.location_api import LocationApi
from src.api.distributor.product_api import ProductApi
from src.api.distributor.rfid_api import RfidApi

class TestReorderControls():
    @pytest.mark.parametrize("conditions", [
        {
            "coefficient": 0,
            "transaction_qty": 1,
            "reorder_qty_coefficient": 3,
            "testrail_case_id": 2581
        },
        { 
            "coefficient": 1,
            "transaction_qty": 1,
            "reorder_qty_coefficient": 2,
            "testrail_case_id": 2582
        },
        {
            "coefficient": 2,
            "transaction_qty": 0,
            "reorder_qty_coefficient": 0,
            "testrail_case_id": 2583
        }
        ])
    @pytest.mark.regression
    def test_create_transaction_at_min_by_ohi_update(self, api, conditions, delete_shipto):
        api.testrail_case_id = conditions["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", "DEFAULT")
        setup_location.add_option("ohi","MAX")
        response_location = setup_location.setup()

        #update OHi
        location_dto = copy.deepcopy(response_location["location"])
        location_dto["onHandInventory"] = response_location["location"]["orderingConfig"]["currentInventoryControls"]["min"]*conditions["coefficient"]
        location_dto["id"] = response_location["location_id"]
        location_list = [copy.deepcopy(location_dto)]
        la.update_location(location_list, response_location["shipto_id"])
        time.sleep(5)
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert len(transaction) == conditions["transaction_qty"], f"The number of transactions should be equal to {conditions['transaction_qty']}"
        if conditions["transaction_qty"] != 0:
            assert transaction[0]["reorderQuantity"] == (response_location["product"]["roundBuy"]*conditions["reorder_qty_coefficient"]), f"Reorder quantity of transaction should be equal to {response_location['product']['roundBuy']*conditions['reorder_qty_coefficient']}"
            assert transaction[0]["product"]["partSku"] == response_location["product"]["partSku"]

    @pytest.mark.parametrize("conditions_issued", [
        {
            "coefficient": 2,
            "transaction_qty": 0,
            "reorder_qty_coefficient": 0,
            "testrail_case_id": 3198
        },
        {
            "coefficient": 0.5,
            "transaction_qty": 1,
            "reorder_qty_coefficient": 2,
            "testrail_case_id": 3197
        }
        ])
    @pytest.mark.regression
    def test_create_transaction_as_issued_by_ohi_update(self, api, conditions_issued, delete_shipto):
        api.testrail_case_id = conditions_issued["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls": "ISSUED"})
        response_location = setup_location.setup()

        #update OHi
        location_dto = copy.deepcopy(response_location["location"])
        location_dto["onHandInventory"] = response_location["location"]["orderingConfig"]["currentInventoryControls"]["max"]*conditions_issued["coefficient"]
        location_dto["id"] = response_location["location_id"]
        location_list = [copy.deepcopy(location_dto)]
        la.update_location(location_list, response_location["shipto_id"])
        time.sleep(5)
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert len(transaction) == conditions_issued["transaction_qty"], f"The number of transactions should be equal to {conditions_issued['transaction_qty']}"
        if conditions_issued["transaction_qty"] != 0:
            assert transaction[0]["reorderQuantity"] == (response_location["product"]["roundBuy"]*conditions_issued["reorder_qty_coefficient"]), f"Reorder quantity of transaction should be equal to {response_location['product']['roundBuy']*conditions_issued['reorder_qty_coefficient']}"
            assert transaction[0]["product"]["partSku"] == response_location["product"]["partSku"]
             
    @pytest.mark.parametrize("conditions_close", [
        {
            "close_transaction_cofficient":2, # MAX > OHI > MIN
            "transaction_qty": 1,
            "close_transaction_qty": 0,
            "reorder_controls": "MIN",
            "testrail_case_id": 3199
        },
        {
            "close_transaction_cofficient":4,
            "transaction_qty": 1,
            "close_transaction_qty": 0,
            "reorder_controls": "ISSUED",
            "testrail_case_id": 3200
        }
        ])
    @pytest.mark.regression
    def test_close_transaction_by_ohi_update(self, api, conditions_close, delete_shipto):
        api.testrail_case_id = conditions_close["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_close['reorder_controls']})
        setup_location.add_option("transaction",'ACTIVE')
        response_location = setup_location.setup()

        #close transaction
        location_dto = copy.deepcopy(response_location["location"])
        location_dto["onHandInventory"] = response_location["location"]["orderingConfig"]["currentInventoryControls"]["min"]*conditions_close["close_transaction_cofficient"]
        location_dto["id"] = response_location["location_id"]
        location_list = [copy.deepcopy(location_dto)]
        la.update_location(location_list, response_location["shipto_id"])
        time.sleep(5)
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction[0]["status"] == "DO_NOT_REORDER"

    @pytest.mark.regression
    def test_update_reorder_quantity_at_min(self, api, delete_shipto):
        api.testrail_case_id = 3201

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls":'MIN'})
        setup_location.add_option("transaction","ACTIVE")
        response_location = setup_location.setup()

        #check quantity
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity_old = transaction[0]["reorderQuantity"]
        #change OHI
        location_dto = copy.deepcopy(response_location["location"])
        location_dto["onHandInventory"] = response_location["location"]["orderingConfig"]["currentInventoryControls"]["min"]*0
        location_dto["id"] = response_location["location_id"]
        location_list = [copy.deepcopy(location_dto)]
        la.update_location(location_list, response_location["shipto_id"])
        time.sleep(5)
        transaction_updated= ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction_updated[0]["reorderQuantity"] == quantity_old + (response_location["location"]["orderingConfig"]["currentInventoryControls"]["min"] - location_dto["onHandInventory"])
       
    @pytest.mark.regression
    def test_update_reorder_quantity_as_issued(self, api, delete_shipto):
        api.testrail_case_id = 3202

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls":'ISSUED'})
        setup_location.add_option("ohi","MAX")
        setup_location.add_option("transaction","ACTIVE")
        response_location = setup_location.setup()

        #check quantity
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity_old = transaction[0]["reorderQuantity"]
        #change OHI
        location_dto = copy.deepcopy(response_location["location"])
        location_dto["onHandInventory"] = response_location["location"]["orderingConfig"]["currentInventoryControls"]["max"]-1
        location_dto["id"] = response_location["location_id"]
        location_list = [copy.deepcopy(location_dto)]
        la.update_location(location_list, response_location["shipto_id"])
        time.sleep(5)
        transaction_updated= ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction_updated[0]["reorderQuantity"] == quantity_old/2

    @pytest.mark.parametrize("conditions_close_by_pack", [
            {
                "pack_conv": 10,
                "reorder_controls": "MIN",
                "testrail_case_id": 3206
            },
            {
                "pack_conv": 2,
                "reorder_controls": "ISSUED",
                "testrail_case_id": 3207
            }
            ])
    @pytest.mark.regression
    def test_close_transaction_by_pack_conversion_update(self, api, conditions_close_by_pack, delete_shipto):
        api.testrail_case_id = conditions_close_by_pack["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)
        pa = ProductApi(api)
        
        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_close_by_pack['reorder_controls']})
        setup_location.add_option("ohi","MAX")
        setup_location.setup_product.add_option("package_conversion", conditions_close_by_pack["pack_conv"])
        setup_location.add_option("transaction",'ACTIVE')
        response_location = setup_location.setup()

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["packageConversion"] = "1"
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated= ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction_updated[0]["status"] == "DO_NOT_REORDER"

    @pytest.mark.parametrize("conditions_create_by_pack", [
            {
                "create_pack_conv":10, 
                "reorder_controls": "MIN",
                "testrail_case_id": 3204
            },
            {
                "create_pack_conv":2,
                "reorder_controls": "ISSUED",
                "testrail_case_id": 3205
            }
            ])
    @pytest.mark.regression
    def test_create_transaction_by_pack_conversion_update(self, api, conditions_create_by_pack, delete_shipto):
        api.testrail_case_id = conditions_create_by_pack["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)
        pa = ProductApi(api)
        
        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_create_by_pack['reorder_controls']})
        setup_location.add_option("ohi","MAX")
        setup_location.setup_product.add_option("package_conversion", "1")
        response_location = setup_location.setup()

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["packageConversion"] = conditions_create_by_pack["create_pack_conv"]
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated= ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction_updated[0]["status"] == "ACTIVE"

    @pytest.mark.parametrize("conditions_update_by_pack", [
            {
                "update_pack_conv":6, 
                "pack_conv": 3,
                "reorder_controls": "MIN",
                "testrail_case_id": 3208
            },
            {
                "update_pack_conv":5,
                "pack_conv": 10,
                "reorder_controls": "ISSUED",
                "testrail_case_id": 3209
            }
            ])
    @pytest.mark.regression
    def test_update_transaction_quantity_by_pack_conversion_update(self, api, conditions_update_by_pack, delete_shipto):
        api.testrail_case_id = conditions_update_by_pack["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)
        pa = ProductApi(api)
        
        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_update_by_pack['reorder_controls']})
        setup_location.add_option("ohi","MAX")
        setup_location.setup_product.add_option("package_conversion", conditions_update_by_pack["pack_conv"])
        setup_location.add_option("transaction",'ACTIVE')
        response_location = setup_location.setup()

        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity_old = transaction[0]["reorderQuantity"]

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["packageConversion"] = conditions_update_by_pack["update_pack_conv"]
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated= ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction_updated[0]["reorderQuantity"] == quantity_old*1.5
    
    @pytest.mark.parametrize("conditions_create", [
        {
            "reorder_controls": "MIN",
            "testrail_case_id": 3494
        },
        {
            "reorder_controls": "ISSUED",
            "testrail_case_id": 3495
        }
        ])
    @pytest.mark.regression
    def test_create_transaction_by_min_max_update(self, api, conditions_create, delete_shipto):
        api.testrail_case_id = conditions_create["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_create['reorder_controls']})
        setup_location.add_option("ohi","MAX")
        response_location = setup_location.setup()

        #create transaction
        location = la.get_locations(shipto_id=response_location["shipto_id"])[0]
        location["orderingConfig"]["currentInventoryControls"]["min"] *= 4
        location["orderingConfig"]["currentInventoryControls"]["max"] *= 4
        la.update_location([location],response_location["shipto_id"])
        time.sleep(5)
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction[0]["status"] == "ACTIVE"

    @pytest.mark.parametrize("conditions_close", [
        {
            "reorder_controls": "MIN",
            "close_coeff_min": 0,
            "close_coeff_max": 1,
            "testrail_case_id": 3496
        }, 
        {
            "reorder_controls": "ISSUED",
            "close_coeff_min": 1,
            "close_coeff_max": 1.5,
            "testrail_case_id": 3497
        }
        ])
    @pytest.mark.regression
    def test_close_transaction_by_min_max_update(self, api, conditions_close, delete_shipto):
        api.testrail_case_id = conditions_close["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_close['reorder_controls']})
        setup_location.add_option("ohi","MAX")
        setup_location.add_option("transaction","ACTIVE")
        response_location = setup_location.setup()

        #close transaction
        location = la.get_locations(shipto_id=response_location["shipto_id"])[0]
        location["orderingConfig"]["currentInventoryControls"]["min"] *=conditions_close["close_coeff_min"]
        location["orderingConfig"]["currentInventoryControls"]["max"] /=conditions_close["close_coeff_max"]
        la.update_location([location],response_location["shipto_id"])
        time.sleep(5)
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        assert transaction[0]["status"] == "DO_NOT_REORDER"
 
    @pytest.mark.parametrize("conditions_update", [
        {
            "reorder_controls": "MIN",
            "testrail_case_id": 3499
        }, 
        {
            "reorder_controls": "ISSUED",
            "testrail_case_id": 3498
        }
        ])
    @pytest.mark.regression
    def test_update_transaction_by_min_max_update(self, api, conditions_update, delete_shipto):
        api.testrail_case_id = conditions_update["testrail_case_id"]

        ta = TransactionApi(api)
        la = LocationApi(api)

        setup_location = SetupLocation(api)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_update['reorder_controls']})
        setup_location.add_option("ohi","0")
        setup_location.add_option("transaction","ACTIVE")
        response_location = setup_location.setup()

        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity_old = transaction[0]["reorderQuantity"]

        #update transaction
        location = la.get_locations(shipto_id=response_location["shipto_id"])[0]
        location["orderingConfig"]["currentInventoryControls"]["min"] +=1
        location["orderingConfig"]["currentInventoryControls"]["max"] +=1
        la.update_location([location],response_location["shipto_id"])
        time.sleep(5)
        transaction_updated = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity = transaction_updated[0]["reorderQuantity"]
        assert transaction_updated[0]["reorderQuantity"] == quantity_old*2

    @pytest.mark.parametrize("conditions_rfid_create", [
        {
            "reorder_controls": "MIN",
            "created_coeff": 300,
            "testrail_case_id": 3642
        }, 
        {
            "reorder_controls": "ISSUED",
            "created_coeff": 50,
            "testrail_case_id": 3643
        }
        ])
    @pytest.mark.regression
    def test_create_transaction_rfid_by_updated_issue_qnt(self, api, conditions_rfid_create, delete_shipto, delete_hardware):
        api.testrail_case_id = conditions_rfid_create["testrail_case_id"]

        ta = TransactionApi(api)
        pa = ProductApi(api)
        ra = RfidApi(api)

        setup_location = SetupLocation(api)
        setup_location.add_option("rfid_location")
        setup_location.add_option("rfid_labels", 1)
        setup_location.setup_product.add_option("issue_quantity",300)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_rfid_create["reorder_controls"]})
        response_location = setup_location.setup()

        ra.update_rfid_label(response_location["location_id"], response_location["rfid_labels"][0]["rfid_id"], "AVAILABLE")

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["issueQuantity"] /= conditions_rfid_create["created_coeff"]
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity = transaction_updated[0]["reorderQuantity"]
        assert transaction_updated[0]["status"] == "ACTIVE"

    @pytest.mark.parametrize("conditions_rfid_update", [
        {
            "reorder_controls": "MIN",
            "testrail_case_id": 3644
        }, 
        {
            "reorder_controls": "ISSUED",
            "testrail_case_id": 3645
        }
        ])
    @pytest.mark.regression
    def test_update_transaction_rfid_by_updated_issue_qnt(self, api, conditions_rfid_update, delete_shipto, delete_hardware):
        api.testrail_case_id = conditions_rfid_update["testrail_case_id"]

        ta = TransactionApi(api)
        pa = ProductApi(api)
        ra = RfidApi(api)

        setup_location = SetupLocation(api)
        setup_location.add_option("rfid_location")
        setup_location.add_option("rfid_labels", 1)
        setup_location.setup_product.add_option("issue_quantity",1)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_rfid_update["reorder_controls"]})
        response_location = setup_location.setup()

        ra.update_rfid_label(response_location["location_id"], response_location["rfid_labels"][0]["rfid_id"], "AVAILABLE")
        transaction = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity_old = transaction[0]["reorderQuantity"]

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["issueQuantity"] *=  product_dto["roundBuy"]
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity = transaction_updated[0]["reorderQuantity"]
        assert quantity_old-quantity == response_location["location"]["orderingConfig"]["currentInventoryControls"]["min"]

    @pytest.mark.parametrize("conditions_rfid_close", [
        {
            "reorder_controls": "MIN",
            "testrail_case_id": 3646
        }, 
        {
            "reorder_controls": "ISSUED",
            "testrail_case_id": 3647
        }
        ])
    @pytest.mark.regression
    def test_close_transaction_rfid_by_updated_issue_qnt(self, api, conditions_rfid_close, delete_shipto, delete_hardware):
        api.testrail_case_id = conditions_rfid_close["testrail_case_id"]

        ta = TransactionApi(api)
        pa = ProductApi(api)
        ra = RfidApi(api)

        setup_location = SetupLocation(api)
        setup_location.add_option("rfid_location")
        setup_location.add_option("rfid_labels", 1)
        setup_location.setup_product.add_option("issue_quantity",1)
        setup_location.setup_shipto.add_option("reorder_controls_settings", {"enable_reorder_control": True,"track_ohi":True, "reorder_controls" :conditions_rfid_close["reorder_controls"]})
        response_location = setup_location.setup()

        ra.update_rfid_label(response_location["location_id"], response_location["rfid_labels"][0]["rfid_id"], "AVAILABLE")

        product_dto = copy.deepcopy(response_location["product"])
        product_dto["issueQuantity"] *= response_location["location"]["orderingConfig"]["currentInventoryControls"]["max"]
        pa.update_product(dto = product_dto, product_id  =response_location["product"]["id"])
        time.sleep(5)
        transaction_updated = ta.get_transaction(shipto_id=response_location["shipto_id"])["entities"]
        quantity = transaction_updated[0]["reorderQuantity"]
        assert transaction_updated[0]["status"] == "DO_NOT_REORDER"