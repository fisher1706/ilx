from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
import time
from common import *

db_keys = get_db_keys()
NUMBER_OF_LOCATIONS = db_keys["number_of_locations_per_shipto"]

with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("select customer.id from srx.customer left join srx.warehouse on warehouse.id = customer.warehouse_id where warehouse.distributor_id = 2 and customer.status = 'ACTIVE' order by customer.id asc")
        fetched_customer_ids = cursor.fetchall()
        customer_ids = get_list(fetched_customer_ids)
        customer_ids = customer_ids[2:11]
        print("Got customers")
        cursor.execute(f"select id, number, name, customer_id from srx.ship_to where customer_id in {tuple(customer_ids)}")
        fetched_shiptos = cursor.fetchall()
        print("Got shiptos")

        d1 = datetime.strptime('1/1/2021', '%d/%m/%Y')
        d2 = datetime.strptime('1/6/2022', '%d/%m/%Y')
        for index, shipto in enumerate(fetched_shiptos):
            cursor.execute(f"select product.part_sku from srx.location left join srx.ordering_config on location.id = ordering_config.location_id left join srx.product on product.id = ordering_config.product_id where location.ship_to_id = {shipto[0]}")
            fetched_product_skus = cursor.fetchall()
            product_skus = get_list(fetched_product_skus)
            usage_history_list = list()
            for product in product_skus:
                for i in range(50):
                    usage_history = {
                        "created_at": now(),
                        "created_by": "LOAD SETUP",
                        "updated_at": now(),
                        "updated_by": "LOAD SETUP",
                        "distributor_id": 2,
                        "customer_id": shipto[3],
                        "order_number": int(time.time()),
                        "ship_to_number": shipto[1],
                        "ship_to_name": shipto[2],
                        "date": random_date(d1, d2),
                        "quantity": random.randint(1, 1000),
                        "part_sku": product
                    }
                    usage_history_tuple = tuple(usage_history.values())
                    usage_history_list.append(usage_history_tuple)
            usage_history_keys = ",".join(usage_history.keys())
            usage_history_values_template = value_template(usage_history)
            usage_history_values = ",".join(cursor.mogrify(f"({usage_history_values_template})", i).decode('utf-8') for i in usage_history_list)
            print("Start insert")
            execute_value = f"INSERT INTO srx.usage_history({usage_history_keys}) VALUES {usage_history_values}"
            cursor.execute(execute_value)
            print(f"Shipto {shipto[0]}")
            conn.commit()
