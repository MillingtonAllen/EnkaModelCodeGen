import json
import queue

from JavaClass import JavaClass
from builder import TypedBuilderFactory
from builder.MemberMerger import merge
from builder.TypedBuilderFactory import is_complex_type, is_map_complex, is_list_complex
from builder.exceptions.exceptions import NotSupportedOnPrimitiveException


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
    def __init__(self, package_name=None):
        self.package_name = package_name

    def str_to_dict(self, json_str: str):
        # return value can be a list or dict, we expect dict
        return json.loads(json_str)

    def traverse_dict(self, input: dict):
        q = queue.Queue()
        built_classes = dict()

        q.put((tuple(), "userDetail", input))

        while not q.empty():
            path, key, value = q.get()
            try:
                built_class = TypedBuilderFactory.create(key, value).build_as_class(self.package_name)
                self.merge_classes(built_classes, path, built_class)
                self.add_children_to_queue(q, path, key, value)
            except NotSupportedOnPrimitiveException as ex:
                pass
        return list(built_classes.values())

    def merge_classes(self, context: dict, path: tuple, incoming_class: JavaClass):
        existing_class = context.get(path)
        if existing_class is not None:
            updated_member_list = merge(incoming_class.members, existing_class.members)
            updated_class = JavaClass(**incoming_class.dict())
            updated_class.members = updated_member_list
            context[path] = updated_class
            return
        context[path] = incoming_class

    def add_children_to_queue(self, q, path, key, payload):
        if not is_complex_type(payload):
            return
        elif is_map(key):  # map must be checked before dict
            if is_map_complex(payload):
                for each in payload.values():
                    for key, value in each.items():
                        if is_complex_type(value):
                            new_path = (*path, key)
                            q.put((new_path, key, value))
        elif is_list(payload):
            if is_list_complex(payload):
                for each in payload:
                    for key, value in each.items():
                        if is_complex_type(value):
                            new_path = (*path, key)
                            q.put((new_path, key, value))
        elif is_dict(payload):
            for key, value in payload.items():
                if is_complex_type(value):
                    new_path = (*path, key)
                    q.put((new_path, key, value))
