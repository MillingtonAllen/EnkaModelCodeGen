import json
import queue
from typing import Any, List

from JavaClass import JavaClass
from JavaMember import JavaMember


def to_pascal_case(input):
    return input[0].upper() + input[1:]


def to_java_primitive_type(input):
    java_type_map = {str: "String", int: "Integer", bool: "Boolean", float: "Double"}
    return java_type_map[type(input)]


def is_map(variable_name):
    return variable_name[-3:] == "Map"


def is_list(input):
    return type(input) is list


def is_dict(input):
    return type(input) is dict


class Parser():
    def __init__(self):
        self.package_name = "com.example.enkaapi.models"

    def str_to_dict(self, json_str: str):
        # return value can be a list or dict, we expect dict
        return json.loads(json_str)

    def traverse_dict(self, input: dict):
        q = queue.Queue()
        ctx = dict()  # str, java_type

        q.put(("userDetail", input))

        while not q.empty():
            key, value = q.get()
            built_class = self.build_class(key, input[key])
            self.merge_class_into_context(ctx, built_class)
            self.add_children_to_queue(q, value)

    def build_class(self, parent_key: str, payload: any) -> JavaClass:

        # TODO handle cases for list and map
        members = self.build_members_for_object(payload)

        built_class = JavaClass(
            class_name=to_pascal_case(parent_key),
            package_name=self.package_name,
            members=members,
        )
        return built_class

    def build_members_for_object(
            self,
            payload: dict  # Change to json_entry class
    ) -> List[JavaMember]:
        members = []
        for key, value in payload.items():
            # TODO validate variable_name and class_name (derived from key) are valid variable name
            # TODO abstract if else chain into typed json_entry classes (inheritance)
            if not self.is_complex_type(value):
                built_member = JavaMember(
                    variable_type=to_java_primitive_type(value),
                    variable_name=key)
            elif is_map(key):  # map must be checked before dict
                pass
            elif is_list(value):
                pass
            elif is_dict(value):
                built_member = JavaMember(
                    variable_type=to_pascal_case(key),
                    variable_name=key)
            else:
                raise RuntimeError("Unexpected Member Type")  # TODO custom error type
            members.append(built_member)
        return members

    def merge_class_into_context(self, ctx, built_class):
        ctx[built_class.class_name] = built_class  # TODO proper merge

    def add_children_to_queue(self, q, payload):
        for key, value in payload.items():
            if self.is_complex_type(value):
                q.put((key, value))

    def is_complex_type(self, input: Any) -> bool:
        if type(input) in [int, float, str, bool]:
            return False
        return True
