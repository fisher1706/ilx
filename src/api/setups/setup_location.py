from src.api.distributor.location_api import LocationApi
from src.api.setups.setup_shipto import setup_shipto
from src.api.setups.setup_product import setup_product
from src.resources.tools import Tools
import copy

def setup_location(context, product_dto=None, shipto_dto=None, location_dto=None, location_pairs=None, location_type="LABEL"):
    la = LocationApi(context)

    product_dto = setup_product(context, product_dto)

    shipto_response = setup_shipto(context, shipto_dto)
    shipto_dto = copy.deepcopy(shipto_response["shipto"])
    new_shipto = shipto_response["shipto_id"]

    if (location_dto is None):
        location_dto = Tools.get_dto("location_dto.json")
        if (location_pairs is None):
            location_dto["attributeName1"] = product_dto["partSku"]
            location_dto["attributeValue1"] = product_dto["partSku"]
        else:
            location_dto["attributeName1"] = location_pairs["attributeName1"]
            location_dto["attributeValue1"] = location_pairs["attributeValue1"]
            location_dto["attributeName2"] = location_pairs["attributeName2"]
            location_dto["attributeValue2"] = location_pairs["attributeValue2"]
            location_dto["attributeName3"] = location_pairs["attributeName3"]
            location_dto["attributeValue3"] = location_pairs["attributeValue3"]
            location_dto["attributeName4"] = location_pairs["attributeName4"]
            location_dto["attributeValue4"] = location_pairs["attributeValue4"]
        location_dto["orderingConfig"] = {
            "product": {
                "partSku": product_dto["partSku"]
            },
            "type": location_type,
            "currentInventoryControls": {
                "min": product_dto["roundBuy"],
                "max": product_dto["roundBuy"]*3
            }
        }
    location_list = [copy.deepcopy(location_dto)]


    la.create_location(copy.deepcopy(location_list), new_shipto)

    response = {
        "product": product_dto,
        "shipto": shipto_dto,
        "location": location_dto,
        "shipto_id": new_shipto
    }

    return copy.deepcopy(response)