from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from common import *

db_keys = get_db_keys()
NUMBER_OF_CUSTOMERS = db_keys["number_of_customers"]

with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        customers_list = list()
        cursor.execute("select customer.id from srx.customer left join srx.warehouse on customer.warehouse_id = warehouse.id where warehouse.distributor_id = 2 and customer.created_by = 'LOAD SETUP'")
        fetched_customer_ids = cursor.fetchall()
        customer_ids = list()
        for fetched_customer_id in fetched_customer_ids:
            customer_ids.append(fetched_customer_id[0])
        shiptos_list = list()
        for customer_id in customer_ids:
            for i in range(20):
                shipto = {
                    "created_at": now(),
                    "created_by": "LOAD SETUP",
                    "updated_at": now(),
                    "updated_by": "LOAD SETUP",
                    "city": "Load city",
                    "line1": "Load line1",
                    "line2": "Load line2",
                    "state": "AL",
                    "zip_code": "Loadzip",
                    "customer_id": customer_id,
                    "is_inactive_distributor_notification_sent": False,
                    "use_default_transaction_submission": False,
                    "use_default_order_close_logic": False,
                    "use_default_replenishment_list_rules": False,
                    "pricing_source": "SRX",
                    "use_default_pricing_source": True,
                    "use_price_cache": True,
                    "multi_locations_enabled": False,
                    "use_default_multi_locations_setting": True,
                    "status": "ACTIVE",
                    "number": f"{i}",
                    "api_warehouse_id": 54,
                    "crib_crawl_flag": False,
                    "vmi_sync_counter": 0,
                    "use_customer_warehouse": False,
                    "used": False
                }
                shipto_tuple = tuple(shipto.values())
                shiptos_list.append(shipto_tuple)
        shipto_keys = ",".join(shipto.keys())
        shipto_values_template = value_template(shipto)
        shipto_values = ",".join(cursor.mogrify(f"({shipto_values_template})", i).decode('utf-8') for i in shiptos_list)
        execute_value = f"INSERT INTO srx.ship_to({shipto_keys}) VALUES {shipto_values}"
        cursor.execute(execute_value)
        conn.commit()
