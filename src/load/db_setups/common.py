from datetime import datetime
import string
import random
import os
import yaml

def get_db_keys():
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path+"/db_keys.yml", "r", encoding="utf8") as read_file:
            return yaml.safe_load(read_file)

def now():
    return f"{datetime.now().date()} {datetime.now().time()}"

def random_string(length=10):
        letters = string.ascii_uppercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

def value_template(entity):
    values_template = str()
    for _ in entity.keys():
        values_template += "%s,"
    return values_template[:-1]

def get_list(list_of_lists):
    simple_list = list()
    for list_in_list in list_of_lists:
        simple_list.append(list_in_list[0])
    return simple_list