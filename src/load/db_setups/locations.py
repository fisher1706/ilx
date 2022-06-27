from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from collections import defaultdict
from common import *

db_keys = get_db_keys()
NUMBER_OF_LOCATIONS = db_keys["number_of_locations_per_shipto"]

with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("select ship_to.id from srx.ship_to left join srx.customer on customer.id = ship_to.customer_id left join srx.warehouse on warehouse.id = customer.warehouse_id where warehouse.distributor_id = 2 and ship_to.status = 'ACTIVE' order by ship_to.id asc")
        fetched_shipto_ids = cursor.fetchall()
        shipto_ids = get_list(fetched_shipto_ids)
        shipto_ids = shipto_ids[7001:10001]
        print("Got shiptos")

        cursor.execute("select id from srx.product where distributor_id = 2")
        fetched_product_ids = cursor.fetchall()
        product_ids = get_list(fetched_product_ids)
        print("Got products")

        locations_list = list()
        locations_count = 0
        number_of_shiptos = len(shipto_ids)
        for index, shipto_id in enumerate(shipto_ids):
            for i in range(NUMBER_OF_LOCATIONS):
                location = {
                    "created_at": now(),
                    "created_by": "LOAD SETUP",
                    "updated_at": now(),
                    "updated_by": "LOAD SETUP",
                    "ship_to_id": shipto_id,
                    "attribute_name1": f"{i}",
                    "attribute_value1": f"{i}",
                    "status": "ACTIVE",
                    "inventory_status": "FROZEN",
                    "inventory_owned": "CUSTOMER",
                    "surplus": False,
                    "lot": True if i%25 == 0 else False,
                    "serialized": True if i%25 == 0 else False,
                    "sync_discrepancy": False,
                    "erp_absent": False,
                    "consignment": False
                }
                locations_count += 1
                location_tuple = tuple(location.values())
                locations_list.append(location_tuple)
            if index%50 == 0 or index == number_of_shiptos-1:
                location_keys = ",".join(location.keys())
                location_values_template = value_template(location)
                location_values = ",".join(cursor.mogrify(f"({location_values_template})", i).decode('utf-8') for i in locations_list)
                print("Start insert")
                execute_value = f"INSERT INTO srx.location({location_keys}) VALUES {location_values}"
                cursor.execute(execute_value)
                print("Finish insert")
                locations_list = list()
                print(f"shipto {index}")
        conn.commit()

        cursor.execute(f"select location.id, ship_to.customer_id from srx.location left join srx.ship_to on ship_to.id = location.ship_to_id where location.ship_to_id in {tuple(shipto_ids)}")
        fetched_locations = cursor.fetchall()
        locations_by_customer = defaultdict(list)
        print("Got locations")
        for fetched_location in fetched_locations:
            locations_by_customer[str(fetched_location[1])].append(fetched_location[0])
        number_of_customers = len(locations_by_customer.keys())
        print("Fetched")
        ordering_configs_list = list()
        for index, customer in enumerate(locations_by_customer.keys()):
            for i, location in enumerate(locations_by_customer[customer]):
                ordering_config = {
                    "created_at": now(),
                    "created_by": "LOAD SETUP",
                    "updated_at": now(),
                    "updated_by": "LOAD SETUP",
                    "customer_id": int(customer),
                    "location_id": location,
                    "product_id": product_ids[i],
                    "current_ic_max": 11,
                    "current_ic_min": 1,
                    "type": "LABEL",
                    "price_updated_at": now(),
                }
                ordering_config_tuple = tuple(ordering_config.values())
                ordering_configs_list.append(ordering_config_tuple)
            del product_ids[0:2000]
            if index%2 == 0 or index == number_of_customers-1:
                ordering_config_keys = ",".join(ordering_config.keys())
                ordering_config_values_template = value_template(ordering_config)
                ordering_config_values = ",".join(cursor.mogrify(f"({ordering_config_values_template})", i).decode('utf-8') for i in ordering_configs_list)
                print("Start insert")
                execute_value = f"INSERT INTO srx.ordering_config({ordering_config_keys}) VALUES {ordering_config_values}"
                cursor.execute(execute_value)
                print("Finish insert")
                ordering_configs_list = list()
                print(f"customer {customer}")
        conn.commit()
