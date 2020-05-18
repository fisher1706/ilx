from src.api.checkout.checkout_api import CheckoutApi

from src.api.distributor.location_api import LocationApi
from src.resources.tools import Tools
import copy

def issue_return_basis(case, shipto_id, product, quantity=None, epc=None, issue_product=None, return_product=None):
    ca = CheckoutApi(case)
    la = LocationApi(case)

    location_response = la.get_location_by_sku(shipto_id, product)
    location = location_response[0]["id"]
    location_type = location_response[0]["orderingConfig"]["type"]

    # check if cart is empry
    cart_response = ca.get_cart()
    if (cart_response["items"] is None):
        case.activity.logger.info(f"Cart is empty")
    elif (cart_response["items"] is not None):
        case.activity.logger.info(f"Cart have {len(cart_response['items'])}, cart will be closed")
        ca.close_cart()
    
    if (location_type == "LABEL"):
        if (issue_product is True):
            ca.checkout_cart(location, location_type, quantity=quantity, issue_product=True)
            cart_response = ca.get_cart()
            location_response[0]["cartItemId"] = cart_response["items"][0]["cartItemId"]
            location_response[0]["quantity"] = quantity
            ca.issue_product(location_response)
        
        if (return_product is True):
            ca.checkout_cart(location, location_type, quantity=quantity, return_product=True)
            cart_response = ca.get_cart()
            location_response[0]["cartItemId"] = cart_response["items"][0]["cartItemId"]
            location_response[0]["quantity"] = quantity
            ca.return_product(location_response)

    if (location_type == "RFID"):
        if (issue_product is True):
            ca.validate_rfid(location, location_type, epc, issue_product=True)
            ca.checkout_cart(location, location_type, epc=epc, issue_product=True)
            cart_response = ca.get_cart()
            location_response[0]["cartItemId"] = cart_response["items"][0]["cartItemId"]
            location_response[0]["quantity"] = 1
            location_response[0]["epc"] = epc
            ca.issue_product(location_response)
        
        if (return_product is True):
            ca.validate_rfid(location, location_type, epc, return_product=True)
            ca.checkout_cart(location, location_type, epc=epc, return_product=True)
            cart_response = ca.get_cart()
            location_response[0]["cartItemId"] = cart_response["items"][0]["cartItemId"]
            location_response[0]["quantity"] = 1
            location_response[0]["epc"] = epc
            ca.return_product(location_response)