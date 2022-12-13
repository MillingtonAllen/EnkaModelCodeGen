import json
import queue

from JavaClass import JavaClass
from typing import Any


class Parser():
    def __init__(self):
        self.package_name = "com.example.enkaapi.models"

    def str_to_dict(self, json_str: str):
        # return value can be a list or dict, we expect dict
        return json.loads(json_str)

    def traverse_dict(self, input: dict):
        q = queue.Queue()
        keys = input.keys()

        current_class = JavaClass(class_name="root", package_name=self.package_name)

        for key in keys:
            if self.is_complex_type(input[key]):
                q.put(key)

    def is_complex_type(self, input:Any) -> bool:
        return False
