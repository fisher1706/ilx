from contextlib import closing
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
import uuid
from common import *

db_keys = get_db_keys()
NUMBER_OF_PRODUCTS = db_keys["number_of_products"]
DISTRIBUTOR_ID = db_keys["distributor_id"]
with closing(psycopg2.connect(dbname='srx_dev', user='srx_dev',
                        password=db_keys["load_password"], host='localhost', port='5434')) as conn:
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        uuids = list()
        ######################################################
        images_list = list()
        for _ in range(NUMBER_OF_PRODUCTS):
            image_uuid = str(uuid.uuid4())
            image = {
                "uuid": image_uuid,
                "original": "-1",
                "values": "{}",
                "state": "PROCESSED",
                "updated_at": now()
            }
            uuids.append(image_uuid)
            images_tuple = tuple(image.values())
            images_list.append(images_tuple)
        image_keys = ",".join(image.keys())
        image_values_template = value_template(image)
        image_values = ",".join(cursor.mogrify(f"({image_values_template})", i).decode('utf-8') for i in images_list)
        execute_value = f"INSERT INTO srx.cached_images({image_keys}) VALUES {image_values}"
        cursor.execute(execute_value)
        ######################################################
        products_list = list()
        for index in range(NUMBER_OF_PRODUCTS):
            product = {
                "created_at": now(),
                "created_by": "LOAD SETUP",
                "updated_at": now(),
                "updated_by": "LOAD SETUP",
                "part_sku": f"LOAD-{datetime.now().date()}-{random_string()}",
                "round_buy": "1",
                "short_description": random_string(),
                "distributor_id": DISTRIBUTOR_ID,
                "lifecycle_status": "ACTIVE",
                "is_asset_flag": False,
                "lot": False,
                "serialized": False,
                "image_uuid": uuids[index]
            }
            product_tuple = tuple(product.values())
            products_list.append(product_tuple)
        product_keys = ",".join(product.keys())
        product_values_template = value_template(product)
        product_values = ",".join(cursor.mogrify(f"({product_values_template})", i).decode('utf-8') for i in products_list)
        execute_value = f"INSERT INTO srx.product({product_keys}) VALUES {product_values}"
        cursor.execute(execute_value)
        ######################################################
        conn.commit()
        