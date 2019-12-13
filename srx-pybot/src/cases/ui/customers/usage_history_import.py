from src.pages.sub.login_page import LoginPage
from src.pages.distributor.usage_history_page import UsageHistoryPage
from src.resources.case import Case
from src.resources.activity import Activity
import random

def usage_history_import(case):
    case.log_name("Usage history import")
    case.testrail_config(case.activity.variables.run_number, 1842)

    try:
        lp = LoginPage(case.activity)
        uhp = UsageHistoryPage(case.activity)
        usage_history_body = uhp.usage_history_body.copy()

        #-------------------
        usage_history_body["Order Number"] = case.random_string_u(10)
        usage_history_body["Customer Number"] = case.random_string_u(10)
        usage_history_body["ShipTo Number"] = case.random_string_u(10)
        usage_history_body["ShipTo Name"] = case.random_string_u(10)
        usage_history_body["Part SKU"] = case.random_string_u(10)
        usage_history_body["Quantity"] = str(random.choice(range(1, 100)))
        usage_history_body["Date"] = "Sun, Dec 30, 2018"
        #-------------------
        usage_history = [
            [usage_history_body["Order Number"], usage_history_body["Customer Number"], usage_history_body["ShipTo Number"], usage_history_body["ShipTo Name"], usage_history_body["Part SKU"], usage_history_body["Quantity"], "2018/12/30 10:15:30"]
        ]
        lp.log_in_distributor_portal()
        uhp.follow_usage_history_url()
        uhp.import_usage_history(usage_history)
        uhp.check_last_usage_history(usage_history_body.copy())

        case.finish_case()
    except:
        case.critical_finish_case()

if __name__ == "__main__":
    usage_history_import(Case(Activity()))