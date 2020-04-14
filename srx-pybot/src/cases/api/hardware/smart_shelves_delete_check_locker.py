from src.pages.sub.login_page import LoginPage
from src.pages.admin.smart_shelves_page import SmartShelvesPage
from src.api.admin.hardware_api import HardwareApi
from src.resources.case import Case
from src.resources.activity import Activity
from src.bases.smart_shelves_basis import smart_shelves_basis
from src.bases.locker_basis import locker_basis
from src.api.admin.smart_shelves_api import SmartShelvesApi
import time
import random

def smart_shelves_delete_check_locker(case):
    case.log_name("Delete shelf and check that Locker door is empty ")
    case.testrail_config(1928)

    try:
        ssa = SmartShelvesApi(case)
        ha = HardwareApi(case)

        # create smart shelf for main distributor
        response = smart_shelves_basis(case)
        locker_body = response["locker"]
        locker_id = locker_body["id"]
        locker = locker_body["value"]
        iothub_body = response["iothub"]

        ssa.delete_smart_shelves(response["smart_shelves_id"])
        locker_conf = ha.get_locker_configuration(locker_id)
        assert (locker_conf[0]["smartShelfHardware"] == None), f"First locker should not have smart shelf with ID {response['smart_shelves_id']}"
        case.finish_case()
    except:
        case.critical_finish_case()

    try:
        ha.delete_hardware(locker_id)
        time.sleep(5)
        ha.delete_hardware(iothub_body["id"])
    except:
        case.print_traceback()

if __name__ == "__main__":
    smart_shelves_delete_check_locker(Case(Activity(api_test=True)))