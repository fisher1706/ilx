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
        for _ in range(NUMBER_OF_CUSTOMERS):
            customer = {
                "created_at": now(),
                "created_by": "LOAD SETUP",
                "updated_at": now(),
                "updated_by": "LOAD SETUP",
                "warehouse_id": 54,
                "type_id": 1,
                "market_type_id": 1,
                "use_default_transaction_submission": False,
                "use_default_order_close_logic": False,
                "use_default_replenishment_list_rules": False,
                "contact_use_default": True,
                "supply_force": False,
                "discrepancy_report_settings": "FULL_REPORT",
                "pricing_source": "SRX",
                "use_default_pricing_source": True,
                "customer_catalog_enabled": False,
                "use_price_cache": True,
                "multi_locations_enabled": False,
                "use_default_multi_locations_setting": True,
                "name": f"LOAD-{datetime.now().date()}-{random_string()}",
                "status": "ACTIVE",
                "number": f"LOAD-{datetime.now().date()}-{random_string()}"
            }
            customer_tuple = tuple(customer.values())
            customers_list.append(customer_tuple)
        customer_keys = ",".join(customer.keys())
        customer_values_template = value_template(customer)
        customer_values = ",".join(cursor.mogrify(f"({customer_values_template})", i).decode('utf-8') for i in customers_list)
        execute_value = f"INSERT INTO srx.customer({customer_keys}) VALUES {customer_values}"
        cursor.execute(execute_value)
        conn.commit()
