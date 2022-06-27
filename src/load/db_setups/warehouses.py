from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from common import *

db_keys = get_db_keys()
NUMBER_OF_WAREHOUSES = db_keys["number_of_warehouses"]
DISTRIBUTOR_ID = db_keys["distributor_id"]

with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        warehouses_list = list()
        for _ in range(NUMBER_OF_WAREHOUSES):
            warehouse = {
                "created_at": now(),
                "created_by": "LOAD SETUP",
                "updated_at": now(),
                "updated_by": "LOAD SETUP",
                "city": "Load city",
                "line1": "Load line1",
                "line2": "Load line2",
                "state": "AL",
                "zip_code": "Loadzip",
                "contact_email": "dprovorov+load@agilevision.io",
                "invoice_email": "dprovorov+load@agilevision.io",
                "name": f"LOAD-{datetime.now().date()}-{random_string()}",
                "status": "ACTIVE",
                "number": f"LOAD-{datetime.now().date()}-{random_string()}",
                "distributor_id": DISTRIBUTOR_ID,
                "zone_id": "America/New_York",
                # "calculate_at_last_day_of_month": False
            }
            warehouse_tuple = tuple(warehouse.values())
            warehouses_list.append(warehouse_tuple)
        warehouse_keys = ",".join(warehouse.keys())
        warehouse_values_template = value_template(warehouse)
        warehouse_values = ",".join(cursor.mogrify(f"({warehouse_values_template})", i).decode('utf-8') for i in warehouses_list)
        execute_value = f"INSERT INTO srx.warehouse({warehouse_keys}) VALUES {warehouse_values}"
        cursor.execute(execute_value)
        conn.commit()
