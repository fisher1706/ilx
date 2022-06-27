from ast import Raise
from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from common import *

db_keys = get_db_keys()

with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        customers_list = list()
        cursor.execute("select customer.id from srx.customer left join srx.warehouse on customer.warehouse_id = warehouse.id where warehouse.distributor_id = 2 and customer.created_by = 'LOAD SETUP'")
        fetched_customer_ids = cursor.fetchall()
        customer_ids = get_list(fetched_customer_ids)


        customer_settings_list = list()
        for customer_id in customer_ids:
            for _ in range(3):
                customer_setting = {
                    "created_at": now(),
                    "created_by": "LOAD SETUP",
                    "updated_at": now(),
                    "updated_by": "LOAD SETUP",
                    "customer_id": customer_id,
                    "use_default": True
                }
                customer_setting_tuple = tuple(customer_setting.values())
                customer_settings_list.append(customer_setting_tuple)
        customer_setting_keys = ",".join(customer_setting.keys())
        customer_setting_values_template = value_template(customer_setting)
        customer_setting_values = ",".join(cursor.mogrify(f"({customer_setting_values_template})", i).decode('utf-8') for i in customer_settings_list)
        execute_value = f"INSERT INTO srx.general_setting({customer_setting_keys}) VALUES {customer_setting_values}"
        cursor.execute(execute_value)

        cursor.execute("select general_setting.id, general_setting.customer_id from srx.customer left join srx.warehouse on customer.warehouse_id = warehouse.id left join srx.general_setting on customer.id = general_setting.customer_id where warehouse.distributor_id = 2 and customer.created_by = 'LOAD SETUP'")
        fetched_customer_settings = cursor.fetchall()
        submit_behavior_list = list()
        order_close_list = list()
        pricing_source_list = list()
        for i in range(0, len(fetched_customer_settings), 3):
            if fetched_customer_settings[i][1] == fetched_customer_settings[i+1][1] == fetched_customer_settings[i+2][1]:
                submit_behavior = {
                    "id": fetched_customer_settings[i][0]
                }
                submit_behavior_tuple = tuple(submit_behavior.values())
                submit_behavior_list.append(submit_behavior_tuple)

                order_close = {
                    "id": fetched_customer_settings[i+1][0]
                }
                order_close_tuple = tuple(order_close.values())
                order_close_list.append(order_close_tuple)

                pricing_source = {
                    "id": fetched_customer_settings[i+2][0],
                    "pricing_source": "SRX",
                    "use_price_cache": True
                }
                pricing_source_tuple = tuple(pricing_source.values())
                pricing_source_list.append(pricing_source_tuple)
            else:
                Raise("something wrong")

        submit_behavior_keys = ",".join(submit_behavior.keys())
        submit_behavior_values_template = value_template(submit_behavior)
        submit_behavior_values = ",".join(cursor.mogrify(f"({submit_behavior_values_template})", i).decode('utf-8') for i in submit_behavior_list)
        execute_value = f"INSERT INTO srx.replenishment_list_submit_behavior({submit_behavior_keys}) VALUES {submit_behavior_values}"
        cursor.execute(execute_value)

        order_close_keys = ",".join(order_close.keys())
        order_close_values_template = value_template(order_close)
        order_close_values = ",".join(cursor.mogrify(f"({order_close_values_template})", i).decode('utf-8') for i in order_close_list)
        execute_value = f"INSERT INTO srx.order_close_settings({order_close_keys}) VALUES {order_close_values}"
        cursor.execute(execute_value)

        pricing_source_keys = ",".join(pricing_source.keys())
        pricing_source_values_template = value_template(pricing_source)
        pricing_source_values = ",".join(cursor.mogrify(f"({pricing_source_values_template})", i).decode('utf-8') for i in pricing_source_list)
        execute_value = f"INSERT INTO srx.pricing_sources_settings({pricing_source_keys}) VALUES {pricing_source_values}"
        cursor.execute(execute_value)

        conn.commit()