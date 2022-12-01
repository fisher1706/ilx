import json
import os
import random
import string
import time

import yaml


class Tools:
    @staticmethod
    def random_email(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        random_email = f"email.{random_string}@agilevision.io"
        return random_email

    @staticmethod
    def get_dto(filename, path="/api/dto/"):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+path
        with open(path+filename, "r", encoding="utf8") as read_file:
            return json.load(read_file)

    @staticmethod
    def get_yaml(filename, path="/"):
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+path
        with open(path+filename, "r", encoding="utf8") as read_file:
            return yaml.safe_load(read_file)

    @staticmethod
    def generate_log(folder, data):
        try:
            with open(folder, 'a', encoding="utf8") as file:
                for entry in data:
                    file.write(str(entry) + '\n')
        except:
            pass

    @staticmethod
    def ymd_dateformat(months):
        return time.strftime("%Y/%m/%d", time.localtime(time.time() + 3600*24*30*months))

    @staticmethod
    def add_to_dict_if_not_none(dictionary, key, value):
        if value is not None:
            dictionary[key] = value
